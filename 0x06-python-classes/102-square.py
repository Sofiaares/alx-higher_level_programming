#!/usr/bin/python3
"""Def a class Sqr"""


class Square:
    """Rep a square"""

    def __init__(self, size=0):
        """Init a new sqr
        Args:
            size (int): The size of the new sqr
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the sqr"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the crnt area of the sqr"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Def the == comparision to a Sqr"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Def the != comparison to a Sqr"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Def the < comparison to a Sqr"""
        return self.area() < other.area()

    def __le__(self, other):
        """Def the <= comparison to a Sqr"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Def the > comparison to a Sqr"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Def the >= compmarison to a Sqr"""
        return self.area() >= other.area()
