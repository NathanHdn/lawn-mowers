# -*- coding: utf-8 -*-

import unittest

from core.orientation import Orientation


class TestOrientation(unittest.TestCase):
    """
    Test the core.orientation.Orientation cless
    """

    def test_init(self):
        """
        Test the instansation of an Orientation object
        """
        o = Orientation('S')
        self.assertTrue(o.is_south())
        self.assertFalse(o.is_north())
        self.assertFalse(o.is_east())
        self.assertFalse(o.is_west())

    def test_bad_arg_value(self):
        """
        Test the the instantiation of an Orientation
        object with a wrong argument value
        """
        self.failUnlessRaises(ValueError, Orientation, "Z")

    def test_left_rotation(self):
        """
        Test the left rotation method
        """
        o = Orientation('N')
        o.rotate_left()
        self.assertTrue(o.is_west())

    def test_right_rotation(self):
        """
        Test the right rotation method
        """
        o = Orientation('N')
        o.rotate_right()
        self.assertTrue(o.is_east())

    def test_to_char(self):
        """
        Test the to_char  method
        """
        o = Orientation('E')
        self.assertEqual(o.to_char(), 'E')


if __name__ == '__main__':
    unittest.main()