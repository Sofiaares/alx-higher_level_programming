#!/usr/bin/python3
"""Def a MagicClass matching exactly a bytecode"""

import math


class MagicClass:
    """Rep a circle."""

    def __init__(self, radius=0):
        """Init a MagicClass.
        Arg:
            radius (float or int): The rad of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Rtn the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circum of the MagicClass."""
        return (2 * math.pi * self.__radius)
