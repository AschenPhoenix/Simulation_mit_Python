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
print('\n\n\n', '\t\t\t Aufgaben - Lineare Gleichungssysteme', '\n')
print('\n\n\n', '\t\t\t Aufgabe a', '\n')
A=np.array([[1,-1,1],[2,1,--1],[-1,-4,3]])
b=np.array([6,-3,14]).T
print(np.linalg.solve(A,b))


print('\n\n\n', '\t\t\t Aufgabe b', '\n')
A=np.array([[1,1,1],[2,-3,4],[3,-2,-2]])
b=np.array([4,33,2]).T
print(np.dot(np.linalg.inv(A),b))


print('\n\n\n', '\t\t\t Aufgabe c', '\n')
A=np.array([[2,1,2],[1,0,1],[4,1,4]])
b=np.array([1,4,0]).T
print(np.dot(np.linalg.pinv(A),b))


print('\n\n\n', '\t\t\t Aufgabe d', '\n')
a=np.pi
b=2.5
c=np.exp(1)
d=0.1
A=np.array([[a,b],[c,d]])
key=np.array([[190.58097349], [143.15889764]])
target=np.linalg.solve(A,key)
print(target)
north=target[0][0]
east=target[1][0]
import webbrowser
#webbrowser.open(f'https://www.google.de/maps/place/{north}+{east}')


print('\n\n\n', '\t\t\t Aufgabe e', '\n')
def funk_pruefen(A,b):
    try:
        if np.linalg.det(A) != 0:
            print("Das Gleichungssystem ist lösbar")
            x = np.linalg.solve(A, b)
            print(f"Die Lösung lautet:\n{x}\n")
        else:
            print("Das Gleichungssystem ist nicht lösbar")
            x = np.linalg.lstsq(A, b, rcond=None)
            print(f"Die Annäherungslösung lautet:\n{x[0]}\n")
    except:
        print("Das Gleichungssystem ist nicht lösbar")
        x = np.linalg.lstsq(A, b, rcond=None)
        print(f"Die Annäherungslösung lautet:\n{x[0]}\n")

# Teil 1
A=np.array([[3,1,1], [8, 0, 7], [8, 0, 9]])
b=np.array([[ 6], [10], [ 2]])
funk_pruefen(A,b)

# Teil 2
A=np.array([[4, 0, 6, 5],[8, 7, 1, 9], [5, 5, 9, 6], [6, 7, 2, 6]])
b=np.array([[8], [4], [1], [8]])
funk_pruefen(A,b)

# Teil 3
A=np.array([ [0.43, 0.20, 0.87, 0.15], [0.23, 0.97, 0.76, 0.61], [0.38, 0.59, 0.47, 0.04] ])
b=np.array([ [0.77], [0.99],[ 0.15] ])
funk_pruefen(A,b)

# Teil 4
A=np.array([ [ 62, -8, 86, 72], [-52, 40, 92, 20], [ 97, 91, 1, -77], [ 57, -25, 2, 74], [-61, 69, 99, -87], [ 60, 1, -11, -91]])
b=np.array([[ 69], [ 60], [-33], [ 6], [ 50], [-60]])
funk_pruefen(A,b)

# Teil 5
A=np.array([ [-28, -90, 52, -49], [8, 98, -13, -97], [-10, 26, 64, -54], [ 82, -98, -81, 46]])
b=np.array([[ 97], [-20], [ 35] ,[-56]])
funk_pruefen(A,b)

# Teil 6
A=np.array([[ 9, -3, 6], [-4, -6, 2], [-7, -5, 0]])
b=np.array([[ 15], [-99], [-51]])
funk_pruefen(A,b)

# Teil 7
A=np.array([[ 1, -8, -6], [-5, -1, 4], [ 5, -9, 9]])
b=np.array( [[ 68], [ 36], [-24]])
funk_pruefen(A,b)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1.0', '\n')
x = np.array([0,1,2,3,4,5])
x2 = np.linspace(0,5,100)
F = np.array([0,940,1554,2069,2438,2509])


















