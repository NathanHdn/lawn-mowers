# -*- coding: utf-8 -*-


class Dimensions():
    """
    The Dimensions  object contain the limits of a grid

    Args:
        bottom_left (tuple of int): coordinates (x, y) of the cell at
                                           the bottom left corner of the grid
        right_upper (tuple of int): coordinates (x,y) of the cell at
                                          the upper right corner of the grid

    Attributes:
        x_min (int): min on x axis of the grid
        x_max (int): max on x axis of the grid
        y_max (int): min on y axis of the grid
        y_min (int): min on y axis of the grid

    """



    def __init__(self, bottom_left: (int, int), right_upper: (int, int)):
        if right_upper[0] < bottom_left[0] or right_upper[1] < bottom_left[1]:            # Checking if the right upper corner is at the right and at the right and at the top of the bottom left corner
            raise ValueError("Invalid corners position")
        self.x_max = right_upper[0]
        self.y_max = right_upper[1]
        self.x_min = bottom_left[0]
        self.y_min = bottom_left[1]


    def include(self, coordinates: (int, int)) -> bool:
        """
        Return if the coordinates is on the grid

        :param:  coordinates (tuple of int): coordinate of a cell

        Raise: coordinates are not tuple of int

        Return: (bool) : if the coordinates is on the grid limit
        """
        return self.x_min <= coordinates[0] <= self.x_max and \
               self.y_min <= coordinates[1] <= self.y_max
