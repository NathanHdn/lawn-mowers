# -*- coding: utf-8 -*-

import unittest

from core.mower import Mower



class TestMower(unittest.TestCase):
    """
    Test of the core.mower.Mower class
    """

    def test_init(self):
        """
        Test Mower.get_coor() method
        """
        m = Mower((1,1),  'N')
        self.assertEqual(m.coordinates, (1, 1))
        self.assertTrue(m.orientation.is_north())

    def test_left_rotation(self):
        """
        Test the left rotation method
        """
        m = Mower((1, 1), 'N')
        m.rotate_left()
        self.assertTrue(m.orientation.is_west())

    def test_right_rotation(self):
        """
        Test the right rotation method
        """
        m = Mower((1, 1), 'N')
        m.rotate_right()
        self.assertTrue(m.orientation.is_east())

    def test_move_forward(self):
        """
        Test the forward move of the Mower
        """
        m = Mower((1, 3), 'W')
        m.move(m.front_coordinates())
        self.assertEqual(m.coordinates, (0, 3))

    def test_to_str(self):
        """
         Test the to_str method
         """
        m = Mower((1, 30), 'W')
        self.assertEqual(m.to_str(), "1 30 W")


if __name__ == '__main__':
    unittest.main()