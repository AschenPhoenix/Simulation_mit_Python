#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                      Vorlesung 00                                     #
#                                                                                       #
#########################################################################################
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
#########################################################################################

# ======================================= nächster Teil =================================
print(f'\n\n=====================\n||  WS2223 - OOP-Aufgabe  ||\n=====================\n')
# =======================================================================================
class FunctionPlot:
    # Aufgabe a
    def __init__(self, func, limits=(0,1), args=None):
        self._func = func
        self._limits = limits
        self._args = args
        self._label = func.__name__

    # Aufgabe b

    @property
    def x(self):
        return np.linspace(self._limits[0], self._limits[1], num=50)

    @property
    def y(self):
        if self._args is None:
            return self._func(self.x)
        else:
            return self._func(self.x, *self._args)

    # Aufgabe c
    def plot(self):
        plt.plot(self.x, self.y, label=self._label)
        plt.legend()

    # Aufgabe d
    # @staticmethod # Ermöglicht den Aufruf einer Methode ohne self oder andere Objekte als übergabe
    def show(self):
        self.plot()
        plt.show()

# Aufgabe e
def f(x, rd=0.1):
    return 3*x - 4*x**3 - rd

# Aufgabe f
plot_objekt = FunctionPlot(f, limits=(0, 0.1))
plot_objekt.show()

# Aufgabe g
new_plot_objekt = FunctionPlot(f, limits=(0, 0.1), args=[0.01])
new_plot_objekt.show()

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f"Vorlesung`s Video weiter bei 00:00:00")
