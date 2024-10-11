import unittest
import cv2
import numpy as np
from Helpers import Helpers

class TestHelpers(unittest.TestCase):

    def setUp(self):
        # Sample image setup (a simple black square image)
        self.image = np.zeros((100, 100, 3), dtype=np.uint8) * 255

        # Sample contour data for grab_contours
        self.contours = [np.array([[[10, 10]], [[20, 10]], [[20, 20]], [[10, 20]]])]
        self.multi_contours = [self.contours, self.contours]

        # Sample points for orders and transform
        self.pts = np.array([[0, 0], [100, 0], [100, 100], [0, 100]], dtype="float32")

    def test_resize(self):
        # Test resizing the image to different dimensions
        resized_image = Helpers.resize(self.image, width=50)
        self.assertEqual(resized_image.shape[1], 50)
        self.assertEqual(resized_image.shape[0], 50)

        resized_image = Helpers.resize(self.image, height=200)
        self.assertEqual(resized_image.shape[1], 200)
        self.assertEqual(resized_image.shape[0], 200)

        # Ensure no changes occur when no width or height is provided
        same_image = Helpers.resize(self.image)
        self.assertEqual(same_image.shape, self.image.shape)

    def test_grab_contours(self):
        # Simulating actual contours as returned by cv2.findContours
        contours, _ = cv2.findContours(np.zeros((100, 100), dtype=np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Test with 2-length contours list (valid test case)
        grabbed_contours = Helpers.grab_contours([contours, None])
        self.assertEqual(grabbed_contours, contours)

        # Test with 3-length contours list (valid test case)
        grabbed_contours = Helpers.grab_contours([None, contours, None])
        self.assertEqual(grabbed_contours, contours)
    def test_orders(self):
        ordered_pts = Helpers.orders(self.pts)
        self.assertEqual(len(ordered_pts), 4)
        
        # Verify correct ordering (top-left, top-right, bottom-right, bottom-left)
        expected_order = np.array([[0, 0], [100, 0], [100, 100], [0, 100]], dtype="float32")
        
        # Checking point by point, numpy does not compare floating point arrays directly with ==.
        self.assertTrue(np.allclose(ordered_pts, expected_order))

    def test_transform(self):
        # Use a white square image to ensure the transformation will show a difference
        self.image = np.ones((100, 100, 3), dtype=np.uint8) * 255  # White square image
        transformed_image = Helpers.transform(self.image, self.pts)
        
        # Ensure the dimensions are correct
        self.assertEqual(transformed_image.shape[0], 100)
        self.assertEqual(transformed_image.shape[1], 100)

        # Check that transformation changes pixel values
        self.assertNotEqual(np.sum(self.image), np.sum(transformed_image))  # Ensure transformation happens

if __name__ == '__main__':
    unittest.main()
