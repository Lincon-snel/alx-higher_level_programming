#!/usr/bin/python3
"""Defines a square.
"""


class Square:
    """Check for TypeError and ValueError
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
