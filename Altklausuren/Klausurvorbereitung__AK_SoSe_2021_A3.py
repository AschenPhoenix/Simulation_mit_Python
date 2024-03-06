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
import datetime

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

class Impfpass:
    def __init__(self):
        self._geimpft = False
        self._genesen = False
        self._getestet = datetime.datetime.now() - datetime.timedelta(hours=25)

    def _set_geimpft(self):
        self._geimpft = True

    def _set_genesen(self):
        self._genesen = True

    def _set_getestet(self):
        self._getestet = datetime.datetime.now()

    def einlass_erlaubt(self):

        now = datetime.datetime.now()
        time_since_last_test = now - self._getestet
        max_time_difference = datetime.timedelta(hours=24)
        last_test_less_one_day = time_since_last_test < max_time_difference

        einlass_erlaubt = self._geimpft or self._genesen
        einlass_erlaubt = einlass_erlaubt or last_test_less_one_day

        return einlass_erlaubt


def create_customers(size):
    """
    Gibt eine Liste mit Impfpässen zurück
    :param size: Anzahl der Impfpässe
    :return: customers: list(Impfpass)
    """
    #  Zufallszahlen
    geimpft = np.random.randint(2, size=size)
    getestet = np.random.randint(2, size=size)
    genesen = np.random.randint(2, size=size)

    customers = []
    for impf, test, nesen in zip(geimpft, getestet, genesen):
        person = Impfpass()
        if impf:
            person.set_geimpft()
        if test:
            person.set_getestet()
        if nesen:
            person.set_genesen()

        customers.append(person)

    return customers

















