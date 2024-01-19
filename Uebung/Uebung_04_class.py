#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Übung 04
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
import Uebung_04_testfunk
#-----------------------
os.system('clear')
os.system('cls')
print("\n\n\n")
#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 1.0   ||\n=====================\n')
#==================================================================================
class Hole:
    # Initial class-attribute:
    name = 'Hole'
    # Typische Anwendungen der klassenvariablen sind counter
    class_counter = 0
    def __init__(self):
        self._center_point = (0, 0)
        Hole.class_counter +=1
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

#========================== Ende =======================================
print("\n\n")
#=======================================================================