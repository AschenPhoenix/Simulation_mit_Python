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

class Beam:
    def __init__(self, modulus, inertia, length, load, z_max):
        """
        Initialise the Beamclass
        :param: modulus  E, inertia I, length l, z_max, load q
        """

        self._modulus = modulus
        self._inertia = inertia
        self._length = length
        self._z_max = z_max
        self._load = load


    @property
    def inertia(self):
        """
        Returns the inertia
        :return: inertia
        """
        return self._inertia

    @inertia.setter
    def inertia(self, value):
        """
        Sets the inertia
        :param value:
        :return:
        """
        self._inertia = value

    @property
    def sigma_max(self):
        """
        Returns the sigma max of the Beam
        :return: sigma_max
        """
        Mb = -self._load*self._length**2/2
        Wb = self._inertia/self._z_max
        sigma_max = Mb/Wb
        return sigma_max

    @property
    def w_max(self):
        """
        Returns the w max of the Beam
        :return:
        """
        w_max = self._load*self._length**4/(8*self._modulus*self._inertia)
        return w_max


def inertia_i_beam(b, t, h, a):
    """
    Berechnet die Trägheit in Z-Richtung für ein I-Profil-Balken
    :param b: Breite
    :param t: Stegbereite
    :param h: Höhe
    :param a: Gurthöhe
    :return: inertia
    """
    I = 1/12 * (b*h**3 - (b-t)*(h-2*a)**3)
    return I

E=90e9
l=80
q=1500
b=0.3
h=1.5
t=0.02
a=0.05

I = inertia_i_beam(b, t, h, a)

I_Profil = Beam(modulus=E,inertia=I, length=l, load=q, z_max=(h/2))
print(f'Die maximale Durchbiegung des Balkens ist:\t w_max\t\t={I_Profil.w_max:10.3}')
print(f'Die maximale Spannung des Balkens ist:\t\t sigma_max\t={I_Profil.sigma_max:10.3}\n')
print(f'Die maximale Durchbiegung des Balkens ist:\t w_max\t\t={I_Profil.w_max}')
print(f'Die maximale Spannung des Balkens ist:\t\t sigma_max\t={I_Profil.sigma_max}')

















