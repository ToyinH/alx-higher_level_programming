#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""
from models.base import Base

class Rectangle(Base):
    """
    class Rectangle that inherits from class Base
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        
        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle.
            x(int, optional): The x parameter
            y(int, optional): The y parameter
            id(int, optional): The ID of the Rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """
        The getter method for width
        
        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter method for width

        Value(int): the value of the width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        The getter method for height

        Returns:
            int: The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter method for height

        Args:
            value(int): The value of the height
        """
        self.__height = value

    @property
    def x(self):
        """
        The setter method for x

        Returns:
            int: returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        The setter method for x

        Args:
            value(int): the value of x
        """
        self.__x = x

    @property
    def y(self):
        """
        The getter method for y

        Returns:
            int: returns self.__y
        """
        return self.__y




        