import numpy as np
import pyfastnoisesimd as fns


def perlin_noise(shape, freq=0.02, octaves=4, lacunarity=2.1, gain=0.45, seed=None, threads=4, normalize=True):
    """
    Generate a numpy array of Perlin noise using the PerlinNoise object.

    Parameters:
    - shape : tuple of int, the shape of the generated array. Must be 2D.
    - octaves : int, the number of layers of noise to combine.
    - seed : int or None, seed for the random generator.

    Returns:
    - numpy.ndarray: A 2D array of Perlin noise values.
    """
    
    if seed is None:
        seed = np.random.randint(2**31)

    perlin = fns.Noise(seed=seed, numWorkers=threads)
    perlin.frequency = freq
    perlin.noiseType = fns.NoiseType.Perlin
    perlin.fractal.octaves = octaves
    perlin.fractal.lacunarity = lacunarity
    perlin.fractal.gain = gain
    perlin.perturb.perturbType = fns.PerturbType.NoPerturb
    result = perlin.genAsGrid(shape)
    if normalize:
        result = (result - result.min()) / (result.max() - result.min())
    
    return result