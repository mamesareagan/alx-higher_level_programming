#!/usr/bin/python3
"""Represent a square.
private instance of  size"""


class Square:
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
