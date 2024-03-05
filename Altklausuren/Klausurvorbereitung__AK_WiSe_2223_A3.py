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


class FunctionsPlot:
    def __init__(self,func,limits=(0,1), args=None):
        """
        Initialisiert ein Objekt der Klasse FunctionPlot
        :param func:
        :param limits:
        :param args:
        """
        self._func = func
        self._limits = limits
        self._args = args
        self._label = func.__name__

    @property
    def x(self):
        return np.linspace(self._limits[0], self._limits[1], 50)

    @property
    def y(self):
        if self._args is not None:
            return self._func(self.x,*self._args)
        else:
            return self._func(self.x)

    def plot(self):
        """
        Anlegen des Plotts der Funktion func für die Werte x
        :return:
        """
        plt.plot(self.x, self.y, label=self._label)

    # ==================== Methoden ========================
    def show(self):
        """
        Erzeugt eines Plotts der Funktion func
        :return: Plot
        """
        import matplotlib.pyplot as plt
        plt.figure(f'Plot der Funktion \"{self._label}\"')
        plt.title(f'Plot der Funktion \"{self._label}\"')
        self.plot()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend(loc='best')
        plt.grid()
        plt.show()

# ##############################################################################

def f(x, rd=0.1):
    return (3*x - 4*x**3 - rd)

wall1 = FunctionsPlot(func=f, limits=(0,0.1))
wall1.show()

wall1 = FunctionsPlot(func=f, limits=(0,0.1), args=(0.001,))
wall1.show()











