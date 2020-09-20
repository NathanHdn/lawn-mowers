# -*- coding: utf-8 -*-

from .orientation import Orientation

class Mower() :
    """
    The Mower object contain its coordinates on the lawn grid
    and its orientation (cardinal point).
    Thr Mower is able to turn left and right and go forward


    Args:
        coordinates (tuple of int): coordinates of the Mower on the lawn, format: (int, int)
        orientation (char): letter corresponding to one of the 4 cardinal points.
                            -> accepted values : {'N', 'E', 'S', 'W'}

    Attributes:
        coor (tuple of int): x and y coordinates of the Mower on the lawn, format: (int, int)
        orient(Orientation): Orientation of the Mower

    """


    def __init__(self, coordinates: (int, int), orientation: chr):
        self.coor: (int, int) = coordinates
        self.orient: Orientation = Orientation(orientation)




    def rotate_left(self):
        """
        Rotate the Mower of 90° at the left

        :param:  None

        :return: None
        """
        self.orient.rotate_left()


    def rotate_right(self):
        """
        Rotate the Mower of 90° at the right

        :param:  None

        :return: None
        """
        self.orient.rotate_right()


    def move(self, coor):
        """
        Move forward the coordinate

        :param:  coordinate (tuple)

        :return: None
        """
        self.coor = coor


    def front_coordinates(self)-> (int, int):
        """
        Return the coordinates of the cell in front of the mower

        :param:  None

        :return: coordinates of the front cell (tuple of int)
        """
        x = self.coor[0]
        y = self.coor[1]
        if self.orient.is_north():
            y += 1
        elif self.orient.is_east():
            x += 1
        elif self.orient.is_south():
            y -= 1
        elif self.orient.is_west():
            x -= 1
        return (x, y)




    def to_str(self) -> str:
        """
        Return a string corresponding to position of the mower,
        format, "'x' 'y' 'orientation'" ex: "10 40 E"

        :param:  None

        :return: the position in a string format, ex: "1 3 N"
        """
        return str(self.coor[0]) + ' ' + \
               str(self.coor[1]) + ' ' + \
               self.orient.to_char()

