__author__ = 'francis'
__author__ = 'francis'
from math import *


def cube_volume(side):
    """
    calculates the volume of a cube given its side length
    >>> cube_volume(10)
    1000
    :param side: side length of the cube
    :return:volume of a cube
    """
    return side * side * side


def pyramid_volume(height, breadth):
    """
    Calculates the volume of a pyramid given its height and breadth
    >>>pyramid_volume(10,12)
    40
    :param height:height of the pyramid
    :param breadth:breadth of the pyramid
    :return:volume of pyramid
    """
    return (1.0/3.0) * height * breadth


def circle_area(radius):
    """
    Determines the area of a circle given its radius
    >>>circle_area(20)
    1256.6371
    :param radius:the radius of a circle
    :return:the area of a circle
    """
    return pi * radius * radius


def circle_area_using_diameter(diameter):
    """
    This calculates the area of a circle
    >>>circle_area_using_diameter(10)
    78.5398
    :param diameter: the diameter of a circle
    :return:the area of the circle
    """
    return (pi * (diameter ** 2))/4.0


def right_circular_cone_lateral_area(radius, height):
    """
    Finds the surface area of a right circular cone
    >>> right_circular_cone_lateral_area(4,10)
    39.7384
    :param radius:radius of the right circular cone
    :param height:height of the right circular cone
    :return:the surface area of the cone
    """
    return pi * radius * math.sqrt(radius ** 2 + height ** 2)


def right_circular_cone_volume(radius, height):
    """
    Finds the volume of a right circular cone given its radius and height
    >>> right_circular_cone_volume(6, 14)
    58.6431
    :param radius: radius:radius of the right circular cone
    :param height: height of the right circular cone
    :return:the volume of the cone
    """
    return (1.0/3.0) * pi * (radius**2) * height


def irregular_prism_volume(breadth, height):
    """
    calculate the volume of an irregular prism given its breadth and length
    >>> irregular_prism_volume(10,12)
    120
    :param breadth: the breadth of an irregular prism
    :param height: the height of an irregular prism
    :return:the volume of an irregular prism
    """
    return breadth * height


def right_circular_cylinder_surface_area(radius, height):
    """
    It determines the surface area of a right circular cylinder
    >>> right_circular_cylinder_surface_area(5,8)
    251.3274
    :param radius: the radius of a right circular cylinder
    :param height: the height of a a right circular cylinder
    :return:the surface area of a right circular cylinder
    """
    return 2 * pi * radius * height


def sphere_area(radius):
    """
    Finds the area of a sphere given its radius
     >>> sphere_area(16)
     3216.9909
    :param radius:the radius of a sphere
    :return:the sphere's area
    """
    return 4 * pi * radius * radius


def trapezium_area(breadth, length, height):
    """
    Determines the area of a trapezium given its breadth,length and height
    >>> trapezium_area(10,15,13)
    25.5
    :param breadth:the breadth of a trapezium
    :param length:the length of a trapezium
    :param height:the height of a trapezium
    :return:the area of a trapezium
    """
    return 0.5 * (breadth + length) * height


def ellipse_area(radius1, radius2):
    """
    It evaluates the area of an ellipse given its two radii
    >>> ellipse_area(6,8)
    150,7964
    :param radius1:the shorter radius of the ellipse
    :param radius2:the longer radius of the ellipse
    :return:the radius of the ellipse
    """
    return pi * radius1 * radius2


def triangle_area(base, height):
    """
    It finds the area of a triangle given the height and the base
    >>>triangle_area(10,15)
    75
    :param base:the base of the triangle
    :param height:the height of the triangle
    :return:the area of a triangle
    """
    return 0.5 * base * height
