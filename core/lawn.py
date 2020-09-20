# -*- coding: utf-8 -*-



from threading import Thread

from .dimensions import Dimensions
from .mower import Mower


class Lawn:
    """
    The Lawn  object represent a lawn field
    divided into a grid to simplify navigation

    Args:
         bottom_left_corner (tuple of int): coordinates (x, y) of the cell at
                                           the bottom left corner of the grid

    Attributes:
        dim (Dimensions Object): The dimensions the grid
        mowers (list of Mower Object): Collection of mowers on the lawn grid  -> see notes
        mowing_list (list of Thread): Collection  of active mowing on the lawn

    Notes:
       -We chose to determine if a cell is free by checking
        on the mower's collection if this cell is not used
        by one of them.
       -Assuming that the numbers of mowers will be significantly
        inferior to the number of free lawn cells, this method
        would offer better performances than implementing a grid.
    """
    def __init__(self, right_upper_corner: (int, int)):
        self.dim = Dimensions((0,0), right_upper_corner)
        self.mowers: list[Mower] = list()
        self.mowing_list: list[Thread] = list()




    def availlable(self, coordinates: (int, int)) -> bool:
        """
        return if the cell at the coordinate in argument is availlable

        :param: coordinates (tuple of int)

        :return: is_availlable (bool)
       """
        if self.dim.include(coordinates):
            return coordinates not in [ m.coor for m in self.mowers ]



    def start_mowing(self, start_coor: (int, int), orientation: str, instructions: str):
        """
        Initialize a Mower Object on lawn at the start position
        then executate then mow following the instruction

        :param:
            start_coor (tuple of int) coordinates of the start position of the mower
            orientation (char): Orientation of the mower (cardinal point)
                                possible values : 'N', 'E', 'W', 'S'
            instructions (str): list of mover's instrucitions

        :return: None
        """
        def execute(instructions: str, mower: Mower):
            #Excecute all the mower's instrcution
            for instruction in instructions:
                instruction.upper()  # ignore case
                if instruction == 'L':
                    mower.rotate_left()
                elif instruction == 'R':
                    mower.rotate_right()
                elif instruction == 'F':
                    destination = mower.front_coordinates()
                    if self.availlable(destination):
                        mower.move(destination)

        if self.availlable(start_coor):
            mower = Mower(start_coor, orientation)
            self.mowers.append(mower)
            mowing = Thread(target=execute, args=(instructions, mower))
            self.mowing_list.append(mowing)
            mowing.start()


    def wait_mowing_end(self):
        """
        Wait until the end of all the mowing proccess
        that are currently happening.

        :param:: None

        :return: None
       """
        for thread in self.mowing_list:  # We wait the end of all mowing
            thread.join()
        self.mowing_list.clear()


    def mowers_positions(self):
        """
        Return a string containing all mowers positions separating by \n

        :param: None

        :return: mowers_position (string)
       """
        mowers_positions = '\n'.join([m.to_str() for m in self.mowers])
        return mowers_positions







