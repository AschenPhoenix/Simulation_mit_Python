#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                       Uebung 05                                       #
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
import copy
from sympy import true
from scipy.interpolate import interp1d
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
print(f'\n\n=========================\n||  Aufgabe 3.0  ||\n=========================\n')
# =======================================================================================
print('\n\n===== Teilaufgabe a =====\n')
A = np.array([[1, -2, 1], [2, 1, -1], [-1, -4, 3]])
b = np.array([6, -3, 14])
x = np.linalg.solve(A, b)
print(f'Lösungsvektor x={x}')


print('\n\n===== Teilaufgabe b =====\n')
A = np.array([[1, 1, 1], [2, -3, 4], [3, -2, -2]])
b = np.array([4, 33, 2])

invA = np.linalg.inv(A)
x = np.dot(invA,b)
print(f'Lösungsvektor x={x}')


print('\n\n===== Teilaufgabe c =====\n')
A = np.array([[2, 1, 2], [1, 0, 1], [4, 1, 4]])
b = np.array([1, 4, 0])

try:
    invA = np.linalg.inv(A)
    singulaer = np.dot(A, invA)

    if singulaer == np.eye(3):
        print(r'Matrix ist Singulär: $A*A^-1 = I$')
        x = np.dot(invA, b)
        print(f'Lösungsvektor x={x}')
    else:
        print(f'Matrix ist ist nicht Singulär, Lösungsvektor x kann daher nicht berechnet werden')

except:
    invA = None
    print(f'Matrix ist nicht Invertierbar, da sie nicht Singulär ist!')


print('\n\n===== Teilaufgabe d =====\n')


print('\n\n===== Teilaufgabe e =====\n')

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Weiter bei Aufgabe 0.0')