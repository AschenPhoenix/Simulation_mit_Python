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
a = np.pi
b = 2.5
c = np.exp(1)
d = 0.1

A = np.array([[a, b], [c, d]])
key = [190.58097349, 143.15889764]

[north, east] = np.linalg.solve(A, key)

import webbrowser
webbrowser.open(f'https://www.google.de/maps/place/{north}+{east}')


print('\n\n===== Teilaufgabe e =====\n')


def sys_loeser(matrix, loeser, number):
    inv = None
    det = None
    sing = None

    try:
        inv = np.linalg.inv(matrix)
        det = np.linalg.det(matrix)
        sing = np.dot(matrix, inv)

    except:
        print(f'Die Matrix A{number} kann nicht regulär gelöst werden!')
        print(f'Lösung über Annäherungsfunktion\n')

    if sing is not (None):
        print(f'Matrix A{number} ist Singulär: A*A^-1 = I = {sing}')
    else: print(f'Matrix A{number} ist nicht Singulär: A*A^-1 != I = {sing}')

    if det is not (None) and det > 0:
        print(f'Determinante der Matrix A{number} ist det={det} > 0')
    else: print(f'Determinante der Matrix A{number} ist det={det} <= 0')

    if inv is not (None):
        print(f'Die Inverse der Matrix A{number} ist invA={inv}')
    else: print(f'Die Inverse der Matrix A{number} kann nicht gebildet werden!')

    if inv is not(None) and det is not(None) and sing is not(None):
        loesung = np.linalg.solve(matrix, loeser)
        print(f'\nDer Lösungsvektor der Matrix A{number} ist: \nx={loesung}\n\n\n')
    else:
        loesung = np.linalg.lstsq(matrix, loeser, rcond=-1)[0]
        print(f'\nDer angenäherte Lösungsvektor der Matrix A{number} ist: \nx={loesung}\n\n\n')
    return loesung


A1 = np.array([[3,1,1], [8, 0, 7], [8, 0, 9]])
b1 = np.array([[6], [10], [ 2]])

A2=np.array([[4, 0, 6, 5],[8, 7, 1, 9], [5, 5, 9, 6], [6, 7, 2, 6]])
b2=np.array([[8], [4], [1], [8]])

A3=np.array([ [0.43, 0.20, 0.87, 0.15], [0.23, 0.97, 0.76, 0.61], [0.38, 0.59, 0.47, 0.04] ])
b3=np.array([ [0.77], [0.99],[ 0.15] ])

A4=np.array([ [ 62, -8, 86, 72], [-52, 40, 92, 20], [ 97, 91, 1, -77], [ 57, -25, 2, 74], [-61, 69, 99, -87], [ 60, 1, -11, -91]])
b4=np.array([[ 69], [ 60], [-33], [ 6], [ 50], [-60]])

A5=np.array([ [-28, -90, 52, -49], [8, 98, -13, -97], [-10, 26, 64, -54], [ 82, -98, -81, 46]])
b5=np.array([[ 97], [-20], [ 35] ,[-56]])

A6=np.array([[ 9, -3, 6], [-4, -6, 2], [-7, -5, 0]])
b6=np.array([[ 15], [-99], [-51]])

A7=np.array([[ 1, -8, -6], [-5, -1, 4], [ 5, -9, 9]])
b7=np.array( [[ 68], [ 36], [-24]])

ablauf_A = [A1, A2, A3, A4, A5, A6, A7]
ablauf_B = [b1, b2, b3, b4, b5, b6, b7]

for i in range(0, len(ablauf_A)):
    sys_loeser(ablauf_A[i], ablauf_B[i], i+1)

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Weiter bei Aufgabe 0.0')