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

    