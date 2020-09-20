# -*- coding: utf-8 -*-


CARDINALS = "NESW"

class Orientation:
    """
    The Orientation object contains a single orientation corresponding to a cardinal point

    Args:
        cardinal_letter (string): corresponding to the first letter of the cardinal point
                    -> accepted values : {'N', 'E', 'S', 'W'}

    Attributes:
        value (int): indicator of the cardinal point:
                        0 : north
                        1 : east
                        2 : south
                        3 : west
    """

    def __init__(self, cardinal_letter: str):
        cardinal_letter.upper() #ignore case
        if cardinal_letter not in CARDINALS:
            raise ValueError("Not a cardinal point, accepted values : {'N", 'E', 'S', 'W')
        self.value: int = CARDINALS.index(cardinal_letter)





    def rotate_right(self):
        """
        Change the orientation to the one at the right.  ex: N -> W, W -> S, ...

        :param:  None

        :return: None
        """

        self.value = (self.value + 1) % 4


    def rotate_left(self):
        """
        Change the orientation  to the one at the left.  ex: N ->.E, W-> N, ...

        :param: None

        :return: None
        """

        self.value = (self.value - 1) % 4


    def to_char(self) -> str:
        """
        Return a uppercase char corresponding at the firt letter name
        of the current orientation. ex if orientation is north -> return 'N'.

        :param: None

        :return: char: the first letter name of the current orientation. (Uppercase)
        """

        return CARDINALS[self.value]


    def is_north(self) -> bool:
        """
        return True if the current orientation is at the north, else return False

        :param: None

        :return: bool: if the current orientation is at the north
        """

        return self.value == 0


    def is_east(self) -> bool:
        """
        return True if the current orientation is at the east, else return False

        :param: None

        :return: bool: if the current orientation is at the east
        """

        return self.value == 1


    def is_south(self) -> bool:
        """
        return True if the current orientation is at the south, else return False

        :param: None

        :return: bool: if the current orientation is at the south
        """

        return self.value == 2


    def is_west(self) -> bool:
        """
        return True if the current orientation is at the west, else return False

        :param: None

        :return: bool: if the current orientation is at the west
        """

        return self.value == 3
