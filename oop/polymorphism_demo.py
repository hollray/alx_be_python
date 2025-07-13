# ALX Exercise on polymorphism_demo.py
import math


class Shape:
    """
    Base class for geometric shapes. 
    Defines the interface for the area calculation.
    """

    def area(self):
        """
        Raises NotImplementedError to ensure derived classes override this method.
        """
        raise NotImplementedError("Subclass must implement the area() method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle (length * width).
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle (pi * radius^2).
        """
        return math.pi * (self.radius ** 2)
