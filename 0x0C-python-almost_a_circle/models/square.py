#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        The class constructor
        
        Args:
            size(int): the size of the Square
            x(int, optional): the x coordinate of Square
            y(int, optional): the y coordinate of Square
            id(int, optional): the Square ID
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The __str__ method"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        ))

    @property
    def size(self):
        """The public getter method for Square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        The setter method for size of Square
        
        Args:
            value(int): value of size of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        The update method for arguments and keyword arguments
        for Square
        
        Args:
            *args: arguments
            **kwargs: keyword arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)