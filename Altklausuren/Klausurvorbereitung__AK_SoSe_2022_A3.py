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
from openpyxl import Workbook
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
print('\n\n\n', '\t\t\t Aufgabe 3', '\n')
from impfpass import Impfpass

class Restaurant:
    def __init__(self,name,seats,area):
        """
        Anlegen eines Restaurantes
        :param name: Restaurantname
        :param seats: Sitzplätze
        :param area: Gastraumfläche m^2
        :param customers: Anzahl Gäste
        """
        self._name = name
        self._seats = seats
        self._area = area
        self._customers = 0

    @property
    def seats(self):
        return self._seats

    @property
    def customers(self):
        return self._customers

    def activate_new_regulation(self, min_area_per_customer):
        self._seats = int(self._area/min_area_per_customer)

    def check_in(self,impfpass):
        if impfpass.einlass_erlaubt():
            if self._seats > 0:
                self._seats -=1
                self._customers +=1
                print(f'\t {self._name}: Access Granted \t\t\t |Seats left:{self._seats:3}/{(self._seats + self._customers):3}|')
            else:
                print(f'\t {self._name}: Restaurant already full \t |Seats left:{self._seats:3}/{(self._seats + self._customers):3}|')

        else:
            print(f'\t {self._name}: Access Denied \t\t\t |Seats left:{self._seats:3}/{(self._seats + self._customers):3}|')

# Aufgabe 3e
from impfpass import create_customers
new_customers = create_customers(60)
# print (new_customers)

JollyBananaTime = Restaurant(name='Jolly Banana Time', seats=60, area=100)
SadBananaTime = Restaurant(name='Sad Banana Time', seats=60, area=100)

SadBananaTime.activate_new_regulation(min_area_per_customer=10)


for customer in new_customers:
    JollyBananaTime.check_in(customer)
print('\n\n')
for customer in new_customers:
    SadBananaTime.check_in(customer)























