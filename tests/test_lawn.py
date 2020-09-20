# -*- coding: utf-8 -*-

import unittest

from core.lawn import Lawn


class TestLawn(unittest.TestCase):
    """
    Test of the core.lawn.Lawn class
    """
    def test_available(self):
        """
        Test Lawn.availlable()
        """
        l = Lawn((2, 2))
        # Set a mower on the lawn at (1, 1)
        l.start_mowing((1, 1), "N", "")
        self.assertFalse(l.available((1, 1)))
        self.assertTrue(l.available((2, 1)))
        self.assertFalse(l.available((3, 1)))

    def test_mowers_positions(self):
        """
        Test of  mowers_positions() method
        """
        l = Lawn((2, 2))
        l.start_mowing((1, 1), 'W', "")
        self.assertEqual(l.mowers_positions(), "1 1 W")

    def test_start_mowing(self):
        """
        Test the Lawn.start_mowing() method

        """
        l = Lawn((5, 5))
        l.start_mowing((1, 2), "N", "LFLFLFLFF")
        l.start_mowing((3, 3), 'E', "FFRFFRFRRF")
        p_1, p_2 = l.mowers_positions().splitlines()
        self.assertEqual(p_1, "1 3 N")
        self.assertEqual(p_2, "5 1 E")

    def test_wait_mowing_end(self):
        """
        Test Lawn.wait_mowing() method

        """
        l = Lawn((2,2))
        # do right<->left moves one million times and then go forward
        instructions = "RL" * pow(10,6) + 'F'
        l.start_mowing((1,1), 'W', instructions)
        # check if the right<->left moves are still processing
        self.assertTrue(l.mowers_positions().startswith("1 1"))
        # wait the end of all instructions
        l.wait_mowing_end()
        # verify if the last move (go forward) have been excecuted
        self.assertEqual(l.mowers_positions(), "0 1 W")
d



if __name__ == '__main__':
    unittest.main()