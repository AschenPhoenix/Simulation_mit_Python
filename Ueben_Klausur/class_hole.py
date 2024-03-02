# |==============| Bibliotheken |==============|
#                     region
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

# |~~~~~~~~~~~~| Main Bibliotheken |~~~~~~~~~~~|
import numpy as np
import math as mth
import scipy as sc
import matplotlib.pyplot as plt
import matplotlib as mplt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import pytest

# |~~~~~~~~~~| Weitere Bibliotheken |~~~~~~~~~~|
import os
import csv
import sys
import serial
from datetime import datetime
import _thread as thread
import time
import random
import openpyxl as opx
from copy import copy
from sympy import true
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp
import scipy.integrate as s_int
import scipy.optimize as opt
# import opencv as cv2

# |~~~~~~~~~~| Terminal vorbereiten |~~~~~~~~~~|
os.system('cls')
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#                   endregion

# |=======| Import aus anderer Dateien |=======|
#                    region
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# import
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#                   endregion

# |=======| Darstellungseinstellungen |========|
mplt.use('Qt5Agg')
np.set_printoptions(suppress=True)
#plt.tight_layout(pad=0.5)

#########################################################################################
class Hole:
    # Initial class-attribute:
    name = 'Hole'
    # Typische Anwendungen der klassenvariablen sind counter
    class_counter = 0

    def __init__(self):
        '''
        Initialise the Class Hole
        :param: self
        :return: None
        '''
        self._center_point = (0, 0)
        Hole.class_counter += 1
        pass

    @property
    def center_point(self):
        return self.center_point

    @center_point.setter
    def center_point(self, value):
        self.center_point = value


class Circle(Hole):
    def __init__(self, radius):
        '''
                             Magische Methode
        - Enhällt alle Attribute der Klasse (guter Programmier Stil)
        - __init__ MUSS in jeder Klasse vorhanden sein
        '''
        # Initial protected attributes
        super().__init__()
        self._radius = 0.0

        # set initial values
        self._radius = radius

    def __repr__(self):
        '''
                             Magische Methode
        - manuelles anpassen der Beschreibung der Klasse im Debug-Fenster
        '''
        representation_str = "Hole of type circle with radius " + str(self.radius) + "mm"
        return representation_str

    def __add__(self, other):
        '''
                             Magische Methode
        - Definiert was passiert, wenn zwei Objekte dieser Klasse addiert werden.
        '''
        new_area = self.area + other.area
        new_radius = np.sqrt(new_area / np.pi)
        new_circle = Circle(radius=new_radius)
        return new_circle

    # -------------------------------------------------

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.area()
        self.circumference()

    @property
    def area(self):
        area = np.pi * self._radius ** 2
        return area

    @property
    def circumference(self):
        circumference = 2 * np.pi * self._radius
        return circumference


#########################################################################################

circle_1 = Circle(radius=0.5)
print(circle_1.radius)
print('\n')
circle_2 = Circle(radius=0.6)
print(circle_2.radius, circle_2.area, circle_2.circumference)

def test_circle_addition():
    '''
    Tests addition of two Circles
    :param: None
    :return: None
    '''
    circle_3 = circle_1 + circle_2
    print(circle_1.radius, circle_1.area, circle_1.circumference)
    print(circle_2.radius, circle_2.area, circle_2.circumference)
    print(circle_3.radius, circle_3.area, circle_3.circumference)

    print('\n\nAutomotiesierte Kontrolle des Programierten Codes')
    # Test ob der programmierte Code acu tut was er tun soll
    # assert np.isclose(circle_3.area, circle_1.area+circle_2.area+0.1), 'Addition of class circle delivers wrong results' #Bewusste Unstimmigkeit, so das eine Fehlermeldung ausgelöst wird
    assert np.isclose(circle_3.area, circle_1.area + circle_2.area), 'Addition of class circle delivers wrong results'


def test_update_circle_radius():
    '''
    Updatet Tests for addition of two Circles
    :param:  None
    :return: None
    '''
    circle_1 = Circle(radius=0.5)
    area_1 = copy(circle_1.area)
    circumference_1 = copy(circle_1.circumference)

    circle_1 = Circle(radius=0.7)
    area_2 = copy(circle_1.area)
    circumference_2 = copy(circle_1.circumference)

    assert not np.isclose(area_1, area_2), 'The area is not supposed to be identical'
    assert not np.isclose(circumference_1, circumference_2), 'The circumference is not supposed to be identical'


test_update_circle_radius()


















