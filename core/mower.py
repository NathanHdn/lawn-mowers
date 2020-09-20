# -*- coding: utf-8 -*-

from .orientation import Orientation

class Mower():
    """
    The Mower object contain its coordinates on the lawn grid
    and its orientation (cardinal point).
    Thr Mower is able to turn left and right and go forward


    Args:
        coordinates (tuple of int): coordinates of the Mower on the lawn, format: (int, int)
        orientation (char): letter corresponding to one of the 4 cardinal points.
                            -> accepted values : {'N', 'E', 'S', 'W'}

    Attributes:
        coordinates (tuple of int): x and y coordinates of the Mower on the lawn, format: (int, int)
        orientation(Orientation): Orientation of the Mower

    """

    def __init__(self, coordinates: (int, int), orientation: str):
        self.coordinates: (int, int) = coordinates
        self.orientation: Orientation = Orientation(orientation)

    def rotate_left(self):
        """
        Rotate the Mower of 90° at the left

        :param:  None

        :return: None
        """
        self.orientation.rotate_left()

    def rotate_right(self):
        """
        Rotate the Mower of 90° at the right

        :param:  None

        :return: None
        """
        self.orientation.rotate_right()

    def move(self, coordinates):
        """
        Move forward the coordinate

        :param:  coordinate (tuple)

        :return: None
        """
        self.coordinates = coordinates

    def front_coordinates(self)-> (int, int):
        """
        Return the coordinates of the cell in front of the mower

        :param:  None

        :return: coordinates of the front cell (tuple of int)
        """
        x = self.coordinates[0]
        y = self.coordinates[1]
        if self.orientation.is_north():
            y += 1
        elif self.orientation.is_east():
            x += 1
        elif self.orientation.is_south():
            y -= 1
        elif self.orientation.is_west():
            x -= 1
        return x, y

    def to_str(self) -> str:
        """
        Return a string corresponding to position of the mower,
        format, "'x' 'y' 'orientation'" ex: "10 40 E"

        :param:  None

        :return: the position in a string format, ex: "1 3 N"
        """
        return str(self.coordinates[0]) + ' ' + \
               str(self.coordinates[1]) + ' ' + \
               self.orientation.to_char()

