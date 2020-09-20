import unittest

from core.dimensions import Dimensions



class TestDimensions(unittest.TestCase):
    """
    Test the core.dimensions.Dimensions class
    """


    def test_init(self):
        """
        Test the instantiation of an Dimension object
        """
        d = Dimensions((0, 10), (5, 15))
        self.assertEqual(d.x_min, 0)
        self.assertEqual(d.x_max, 5)
        self.assertEqual(d.y_min, 10)
        self.assertEqual(d.y_max, 15)


    def test_bad_init(self):
        """
        Test the instantiation of a Dimension object
        with the right upper corner at the left and/or top
        of the bottom left corner
        """
        self.failUnlessRaises(ValueError, Dimensions, (5, 15),(0, 10))
        self.failUnlessRaises(ValueError, Dimensions, (5, 15), (6, 10))
        self.failUnlessRaises(ValueError, Dimensions, (5, 15), (0, 17))


    def test_include_method(self):
        """
        Test the include method
        """
        d = Dimensions((0, 0), (5, 5))
        self.assertFalse(d.include((6, 1)))
        self.assertTrue(d.include((3, 3)))



if __name__ == '__main__':
    unittest.main()