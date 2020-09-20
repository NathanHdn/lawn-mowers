# -*- coding: utf-8 -*-

import unittest
from core.lawn import Lawn

class TestLawn(unittest.TestCase):
    """
    Test of the main.Mower class
    """
    def test_availlable(self):
        """
        Test Lawn.availlable()
        """
        l = Lawn((2, 2))
        l.start_mowing((1, 1), "N", "") #A mower in now on the lawn at (1, 1)
        self.assertFalse(l.availlable((1,1)))
        self.assertTrue(l.availlable((2, 1)))
        self.assertFalse(l.availlable((3, 1))) #outside the lawn


    def test_mowers_positions(self):
        """
        Test of  mowers_positions() method
        """
        l = Lawn((2, 2))
        l.start_mowing((1, 1), 'W', "")
        self.assertEqual(l.mowers_positions(), "1 1 W")


    def test_start_mowing(self):
        """
        Test the start_mowing()

        """
        l = Lawn((5, 5))
        l.start_mowing((1, 2), "N", "LFLFLFLFF")
        l.start_mowing((3, 3), 'E', "FFRFFRFRRF")
        p_1, p_2 = l.mowers_positions().splitlines()
        self.assertEqual(p_1, "1 3 N")
        self.assertEqual(p_2, "5 1 E")

    def test_wait_mowing_end(self):
        """
        Test Mower.get_coor() method
        Note: very long
        """
        l = Lawn((2,2))
        instructions = "RL" * pow(10,6) + 'F' #We do right<->left one million times and then go forward
        l.start_mowing((1,1), 'W', instructions)
        self.assertEqual(l.mowers_positions()[:3], "1 1")#the instruction are still processing we don't if the orientation is W or E
        l.wait_mowing_end() #we admit that the comper won't have finish to proccess 2 million instructions
        self.assertEqual(l.mowers_positions(), "0 1 W")



if __name__ == '__main__':
    unittest.main()