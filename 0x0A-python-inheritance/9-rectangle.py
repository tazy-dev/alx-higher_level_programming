#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the  Rectangle.
            height (int): The height of the  Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[self.__class__.__name__] {self.__width}/{self.__height}"
