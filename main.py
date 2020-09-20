# -*- coding: utf-8 -*-
import sys
import os
from core.lawn import Lawn


DEFAULT_FILE = os.path.join(os.path.dirname(__file__), 'input/default.txt')

def paired(iterable):
    """
    paired elements of a collections two by tow
    ex: paired([a, b, c, d]) -> [(a, b), (b, c)]

    :param: iterable
    :return collection of tuple of str (zip)
    """
    return zip(*[iter(iterable)] * 2)


def start(file_path):
    """
    read the input file, instantiate the lawn and run every mower simulations

    :param: iterable

    :return: None
    """
    file = open(file_path, "r")
    #The first line of the file contain the rigth  upper corner of the lawn at the format "x y"
    first_line = file.readline()
    #The other lines alternate the start position of the mower and its instructions
    other_lines = file.read().splitlines()
    right_upper_corner = tuple(map(int, first_line.split())) #Coordinate represented by a tuple of 2 ints
    lawn = Lawn(right_upper_corner) #Creation of the lawn
    for start_position, instructions in paired(other_lines):
        x_str, y_str, orientation = start_position.split()
        start_coor = (int(x_str), int(y_str)) #start coordonate of the mower
        lawn.start_mowing(start_coor, orientation, instructions) #start a simulation of a mower
    lawn.wait_mowing_end() #We wait until all mowers finish their instructions
    print(lawn.mowers_positions()) #We print the final position of each mower


if __name__ == '__main__':
    if len(sys.argv) == 1:  #If no specific file_path are in argument
        start(DEFAULT_FILE) #we use the defaul file
    else:
        start(sys.argv[1]) #If a specific file is in argument

