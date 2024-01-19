#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Übung 04
#
#_______________________________________________________________________
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pytest
# -----------------------
import os
import csv
import sys
import serial
from datetime import datetime
import _thread as thread
import time
from copy import copy
from sympy import true
import cv2
# -----------------------
import Uebung_04_testfunk
import Uebung_04_class

# -----------------------
# os.system('clear')
os.system('cls')
print("\n\n\n")
# ======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 1.0   ||\n=====================\n')


# ==================================================================================
class Hole:
    """
    Hole describes a general hole
    """

    name = 'Hole'
    class_counter = 0

    def __init__(self):
        """
        Initialising an instance of the class hole sets the centre point of the hole at the coordinates (0/0)
        """
        Hole.class_counter += 1
        self._centre_point = (0, 0)
        pass

    @property
    def centre_point(self):
        """
        The centre point of the hole
        :return: _centre_point: tuple
        """
        return self._centre_point

    @centre_point.setter
    def centre_point(self, value):
        """

        :param value: tuple
        """
        self._centre_point = value


class Circle(Hole):
    """
    This class represents a circle
    """

    def __init__(self, radius):
        """

        :param radius: float
        """
        # Initialise protected attributes
        super().__init__()
        self._radius = 0.0
        self._radius_intended = 0.0

        # Set initial values
        self.radius = radius

    def __repr__(self):
        """
        How python shows an instance of type Circle
        :return: representation_string: str
        """
        representation_string = "Hole of type circle with radius: " + str(self._radius) + "mm"
        return representation_string

    def __add__(self, other):
        """
        Two circles are added by adding their area
        :param other: Circle
        :return: new_circle: Circle
        """
        new_area = self.area + other.area
        new_radius = np.sqrt(new_area / np.pi)
        new_circle = Circle(radius=new_radius)
        return new_circle

    @property
    def radius(self):
        """
        The radius of the circle
        :return: _radius: float
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        The radius of the circle
        :param value: float
        """
        self._radius = value

    @property
    def area(self):
        """
        The area of the circle
        :return: area: float
        """
        area = np.pi * self._radius ** 2
        return area

    @property
    def circumference(self):
        """
        The circumference of the circle
        :return: circumference: float
        """
        circumference = 2 * np.pi * self._radius
        return circumference

    @property
    def radius_intended(self):
        """
        The intended radius of the circle: may differ from the actual radius of the circle
        :return: _radius_intended: float
        """
        return self._radius_intended

    @radius_intended.setter
    def radius_intended(self, value):
        """
        The intended radius of the circle: may differ from the actual radius of the circle
        :param value: float
        """
        array_radii_intended = np.asarray(value)
        idx = (np.abs(array_radii_intended - 0.05 - self.radius)).argmin()
        self._radius_intended = array_radii_intended[idx]


class Square(Hole):
    """
    This class represents a square
    """

    def __init__(self, edge):
        """

        :param radius:
        """
        # Initialise protected attributes
        super().__init__()
        self._edge = 0.0

        # Set initial values
        self.edge = edge

    def __repr__(self):
        representation_string = "Hole of type square with edge: " + str(self.edge) + "mm"
        return representation_string

    def __add__(self, other):
        new_area = self.area + other.area
        new_edge = np.sqrt(new_area)
        new_circle = Square(edge=new_edge)
        return new_circle

    @property
    def edge(self):
        return self._edge

    @edge.setter
    def edge(self, value):
        self._edge = value

    @property
    def area(self):
        area = self.edge ** 2
        return area

    @property
    def circumference(self):
        circumference = 4 * self.edge
        return circumference


# ====================================================================================================================


class HoleDetection:
    def __init__(self, filename, filepath):
        self._filename = filename
        self._filepath = filepath
        self._image = None
        self._hole_list = []

    @property
    def filename(self):
        return self._filename

    @property
    def filepath(self):
        return self._filepath

    @property
    def image_path(self):
        image_path = self._filepath + self._filename
        return image_path

    @property
    def image(self):
        if self._image is None:
            original_image = cv2.imread(self.image_path, 1)
            grey_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            blur_image = cv2.medianBlur(grey_image, 5)
            self._image = blur_image
        return self._image

    @.setter
    def(self, value):
        pass
#========================== Ende =======================================
print("\n\n")
#=======================================================================