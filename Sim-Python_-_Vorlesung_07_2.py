#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 05
#
#_______________________________________________________________________
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib.ticker import MultipleLocator
import pytest
#-----------------------
import os
import csv
import sys
import serial
from datetime import datetime
import _thread as thread
import time
from copy import copy

from sympy import true
#-----------------------
os.system('clear')
os.system('cls')
print("\n\n\n")
#======================================== Teil 01 =================================
print(f'\n\n=====================\n||     Thema 1     ||\n=====================\n')
#==================================================================================
radius_c1=0.7
area_c1=np.pi*radius_c1**2
circumference_c1=2*np.pi*radius_c1

class Circle:
    def __init__(self, radius):
        '''
                             Magische Methode
        - Enthält alle Attribute der Klasse (guter Programming-Stil)
        - __init__ MUSS in jeder Klasse vorhanden sein
        '''
        # Initial protected attributes
        self._radius=0.0

        # set initial values
        self._radius = radius

    def __repr__(self):
        '''
                             Magische Methode
        - manuelles anpassen der Beschreibung der Klasse im Debug-Fenster
        '''
        representation_str = "Hole of type circle with radius " + str(self.radius) + "mm"
        return representation_str
    
    def __add__(self,other):
        '''
                             Magische Methode
        - Definiert was passiert, wenn zwei Objekte dieser Klasse addiert werden.
        '''
        new_area = self.area + other.area
        new_radius = np.sqrt(new_area/np.pi)
        new_circle = Circle(radius=new_radius)
        return new_circle
    #-------------------------------------------------

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
        area=np.pi*self._radius**2
        return area
    
    @property
    def circumference(self):
        circumference = 2*np.pi*self._radius
        return circumference



circle_1=Circle(radius=0.5)
print(circle_1.radius)
print('\n')
circle_2=Circle(radius=0.6)
print(circle_2.radius, circle_2.area, circle_2.circumference)


#======================================== Teil 01 =================================
print(f'\n\n=====================\n||     Thema 2     ||\n=====================\n')
#==================================================================================
def test_circle_addition():
    circle_3 = circle_1 + circle_2
    print(circle_1.radius, circle_1.area, circle_1.circumference)
    print(circle_2.radius, circle_2.area, circle_2.circumference)
    print(circle_3.radius, circle_3.area, circle_3.circumference)


    print('\n\nAutomotiesierte Kontrolle des Programierten Codes')
    # Test ob der programmierte Code acu tut was er tun soll
    #assert np.isclose(circle_3.area, circle_1.area+circle_2.area+0.1), 'Addition of class circle delivers wrong results' #Bewusste Unstimmigkeit, so das eine Fehlermeldung ausgelöst wird
    assert np.isclose(circle_3.area, circle_1.area+circle_2.area), 'Addition of class circle delivers wrong results'
test_circle_addition()



#======================================== Teil 01 =================================
print(f'\n\n=====================\n||     Thema 3     ||\n=====================\n')
#==================================================================================
def test_update_circle_radius():
    circle_1 = Circle(radius=0.5)
    area_1 = copy(circle_1.area)
    circumference_1 = copy(circle_1.circumference)

    circle_1 = Circle(radius=0.7)
    area_2 = copy(circle_1.area)
    circumference_2 = copy(circle_1.circumference)

    assert not np.isclose(area_1, area_2),'The area is not supposed to be identical'
    assert not np.isclose(circumference_1,circumference_2),'The circumference is not supposed to be identical'
test_update_circle_radius()
#======================================== Teil 02 =================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
#==================================================================================


#========================== Ende =======================================
print("\n\n")
#=======================================================================