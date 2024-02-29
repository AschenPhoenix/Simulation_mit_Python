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

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 0.0', '\n')
Alexander = {'Vorwissen': int(7), 'Programmiersprachen': ['C++', 'Matlab', 'Python'], 'Erwartungen':'Bestehen der Klausur' }
print(Alexander)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1.0', '\n')

string = ''
for j in range(1,10):
    for i in range(1,10):
        string += str(j*i) + '\t'
    string += '\n'
print(string)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2.0', '\n')
string = "56,756,756,7,452,34534,7,65,845,35,345,37,56,3,3,523,1,235,135,57,857,845,745,632,56,58,568,5,1"
print(string)
string=string.replace(',','.')
print(string)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 3.0', '\n')
liste=np.arange(1,42.1,0.1)
print(liste)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 4.0', '\n')
n=50
liste=[]
zeilen=range(len(liste))
for j in range(n):
    liste.append(np.random.randint(1,1000))
for i in zeilen:
    if (liste[i] % 2) !=0:
        del liste[i]
        del zeilen[-1]
print(liste)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 5.0', '\n')















