import os
import numpy as np
import tiff
import scipy.ndimage
import cv2
from skimage import measure


class ImageProcessor:
    def __init__(self, superpixel_size, patch_size, tile_size=32):
        self.superpixel_size = superpixel_size
        self.patch_size = patch_size
        self.tile_size = tile_size

    def load_image(self, image_path):
        image = tiff.imread(image_path)
        return image

    def load_mask(self, mask_path):
        mask = np.load(mask_path)
        if 'mask' in mask:
            mask = mask['mask']
        else:
            mask = mask['arr_0']
        return mask

    def load_image_and_mask(self, image_path, mask_path):
        image = self.load_image(image_path)
        mask = self.load_mask(mask_path)
        return image, mask

    def find_bounding_box(self, mask):
        rows = np.any(mask, axis=1)
        cols = np.any(mask, axis=0)
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        return rmin, rmax, cmin, cmax

    def pad_to_patch_size(self, rmin, rmax, cmin, cmax):
        r_pad = (self.patch_size - (rmax - rmin + 1) % self.patch_size) % self.patch_size
        c_pad = (self.patch_size - (cmax - cmin + 1) % self.patch_size) % self.patch_size
        rmax += r_pad
        cmax += c_pad
        return rmin, rmax, cmin, cmax

    def extract_patches(self, image, mask, rmin, rmax, cmin, cmax):
        patches = []
        labels = []
        coordinates = []

        num_patches_r = (rmax - rmin + self.patch_size) // self.patch_size
        num_patches_c = (cmax - cmin + self.patch_size) // self.patch_size

        image = image[rmin:rmax, cmin:cmax]
        mask = mask[rmin:rmax, cmin:cmax]

        padded_image = np.pad(image, ((0, self.patch_size - (rmax - rmin) % self.patch_size),
                                      (0, self.patch_size - (cmax - cmin) % self.patch_size)),
                              mode='constant')
        padded_mask = np.pad(mask, ((0, self.patch_size - (rmax - rmin) % self.patch_size),
                                    (0, self.patch_size - (cmax - cmin) % self.patch_size)),
                             mode='constant')

        for i0 in range(0, num_patches_r, self.tile_size):
            for j0 in range(0, num_patches_c, self.tile_size):
                for i in range(i0, min(i0 + self.tile_size, num_patches_r)):
                    for j in range(j0, min(j0 + self.tile_size, num_patches_c)):
                        patch_image = padded_image[i * self.patch_size:(i + 1) * self.patch_size,
                                                   j * self.patch_size:(j + 1) * self.patch_size]
                        patch_mask = padded_mask[i * self.patch_size:(i + 1) * self.patch_size,
                                                 j * self.patch_size:(j + 1) * self.patch_size]

                        measure_labels = measure.label(patch_mask)
                        regions = measure.regionprops(measure_labels)

                        if len(regions) == 0:
                            continue
                        patches.append(patch_image)
                        labels.append(patch_mask)
                        coordinates.append((i * self.patch_size, j * self.patch_size))

        return patches, labels, coordinates

    def reassemble_image(self, patches, coordinates, original_shape):
        reassembled_image = np.zeros(original_shape, dtype=patches[0].dtype)

        for patch, (r, c) in zip(patches, coordinates):
            reassembled_image[r:r + self.patch_size, c:c + self.patch_size] = patch

        return reassembled_image

    def process_single_image_into_superpixels(self, image_path, mask_path, output_dir):
        image, mask = self.load_image_and_mask(image_path, mask_path)
        rmin, rmax, cmin, cmax = self.find_bounding_box(mask)
        rmin, rmax, cmin, cmax = self.pad_to_patch_size(rmin, rmax, cmin, cmax)

        patches, labels = self.extract_patches(image, mask, rmin, rmax, cmin, cmax)

        img_name = os.path.splitext(os.path.basename(image_path))[0]
        for idx, (patch, label) in enumerate(zip(patches, labels)):
            patch_output_path = os.path.join(output_dir, "patches", f'{img_name}_patch_{idx}.tif')
            label_output_path = os.path.join(output_dir, "masks", f'{img_name}_patch_{idx}.npz')
            self.save_superpixels(patch, label, patch_output_path, label_output_path)

    def save_superpixels(self, image, mask, image_path, mask_path):
        tiff.imwrite(image_path, image)
        np.savez_compressed(mask_path, mask)

    def block_view(self, A, block_shape):
        shape = (
            A.shape[0] // block_shape[0],
            A.shape[1] // block_shape[1]) + block_shape
        strides = (
            block_shape[0] * A.strides[0],
            block_shape[1] * A.strides[1]) + A.strides
        return np.lib.stride_tricks.as_strided(A, shape=shape, strides=strides)

    def calculate_snr(self, image):
        blocks = self.block_view(image, (self.patch_size, self.patch_size))
        flattened_blocks = blocks.reshape(-1, self.patch_size, self.patch_size)
        means = np.mean(flattened_blocks, axis=(1, 2))
        stds = np.std(flattened_blocks, axis=(1, 2)) + 1e-5
        snr_values = means / stds
        snr_map = snr_values.reshape(blocks.shape[0], blocks.shape[1])
        return snr_map

    def smooth_snr_map(self, snr_map, kernel_size=4):
        kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
        smoothed_snr_map = scipy.ndimage.convolve(snr_map, kernel, mode='constant', cval=0.0)
        return smoothed_snr_map

    def gen_mask(self, image, threshold):
        mask = np.zeros_like(image)
        mask[image > threshold] = 1
        return mask

    def expand_mask(self, mask):
        expanded_mask = np.kron(mask, np.ones((self.patch_size, self.patch_size)))
        return expanded_mask

    def process_image(self, image):
        image = np.array(image)
        image = (image - np.min(image)) / (np.max(image) - np.min(image))
        img = self.smooth_snr_map(self.calculate_snr(image))
        mean, std = np.mean(img), np.std(img)
        mask = self.gen_mask(img, mean + 0.5 * std)
        mask = self.expand_mask(mask)
        pad_height = (image.shape[0] - mask.shape[0] % image.shape[0]) % image.shape[0]
        pad_width = (image.shape[1] - mask.shape[1] % image.shape[1]) % image.shape[1]
        mask = np.pad(mask, ((0, pad_height), (0, pad_width)), mode='constant', constant_values=0)
        image = image * mask
        image = cv2.normalize(image, None, 0, int(2 ** 16 - 1), cv2.NORM_MINMAX).astype(np.uint16)
        if not image.any():
            return None, None
        return image, mask

    def prepare_mask(self, mask, category):
        mask = mask.astype(np.uint8)
        mask *= category
        return mask
