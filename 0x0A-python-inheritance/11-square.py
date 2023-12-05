#!/usr/bin/python3
"""Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """init area"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size ** 2

    def __str__(self) -> str:
        """str"""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
