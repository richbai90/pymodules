import numpy as np
import unittest
from common.datastructures import EnhancedDataKDTree

class TestEnhancedDataKDTree(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        self.points = np.array([[1, 2], [3, 4], [5, 6]])
        self.data = ['A', 'B', 'C']
        self.tree = EnhancedDataKDTree(self.points, self.data)

    def test_query_single_point(self):
        # Test querying a single point
        query_point = np.array([1, 2])
        expected_result = ([0.0], [0], ['A'])
        result = self.tree.query(query_point)
        self.assertEqual(result, expected_result)

    def test_query_multiple_points(self):
        # Test querying multiple points
        query_points = np.array([[1, 2], [3, 4]])
        expected_result = ([0.0, 0.0], [0, 1], ['A', 'B'])
        result = self.tree.query(query_points)
        
        expected_result = (np.array([expected_result[0]]), np.array([expected_result[1]], dtype=int), np.array([[i] for i in expected_result[2]], dtype='<U1'))

        # Compare element-wise
        for i in range(len(expected_result)):
            if isinstance(expected_result[i][0], float):
                self.assertTrue(np.allclose(result[i], expected_result[i]))
            else:
                self.assertTrue(np.array_equal(result[i], expected_result[i]))

    def test_query_k_nearest_neighbors(self):
        # Test querying k nearest neighbors
        query_point = np.array([1, 2])
        k = 2
        expected_result = ([0.0, 2.82842712], [0, 1], ['A', 'B'])
        result = self.tree.query(query_point, k=k)
        
        expected_result = (np.array([expected_result[0]]), np.array([expected_result[1]], dtype=int), np.array([[i] for i in expected_result[2]], dtype='<U1'))

        # Compare element-wise
        for i in range(len(expected_result)):
            if isinstance(result[i][0], float):
                self.assertTrue(np.allclose(result[i], expected_result[i]))
            else:
                self.assertTrue(np.array_equal(result[i], expected_result[i]))
        

    def test_query_return_distance_false(self):
        # Test querying without returning distances
        k=2
        query_point = np.array([1, 2])
        expected_result = ([0, 1], ['A', 'B'])
        result = self.tree.query(query_point, k=2, return_distance=False)

        expected_result = (np.array([expected_result[0]]), np.array([expected_result[1]], dtype=int), np.array([[i] for i in expected_result[2]], dtype='<U1'))

        # Compare element-wise
        for i in range(len(expected_result)):
            if isinstance(expected_result[i][0], float):
                self.assertTrue(np.allclose(result[i], expected_result[i]))
            else:
                self.assertTrue(np.array_equal(result[i], expected_result[i]))
        

    def test_custom_mapping_function(self):
        # Test using a custom mapping function
        def mapping_function(point, _):
            # Find the index that holds the query point
            return np.argmin(np.linalg.norm(self.points - point, axis=1))
        query_point = np.array([1, 2])
        expected_result = ([0.0], [0], ['A'])
        tree = EnhancedDataKDTree(self.points, self.data, mapping_function=mapping_function)
        result = tree.query(query_point)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()