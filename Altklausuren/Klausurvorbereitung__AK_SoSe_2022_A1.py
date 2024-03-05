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
# np.set_printoptions(suppress=True)
#plt.tight_layout(pad=0.5)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1a)', '\n')
#F15_10 = np.loadtxt(r'C:\Users\alex-\OneDrive\Uni und Verbindung\Uni und aktuelles Semester\Aktuelles Semester\WiSe 2324 - Simulation technischer Systeme mit Python\Eigene Programme\Simulation_mit_Python\Altklausuren\SS2022\F15_10.DAT')
x = np.array(np.loadtxt(r'F15_10.DAT', skiprows=3, usecols=0))
y = np.array(np.loadtxt(r'F15_10.DAT', skiprows=3, usecols=1))

plt.figure()
plt.plot(x,y)
plt.xlabel('Horizontale Koordinaten')
plt.ylabel('Vertikale Koordinaten')
plt.axis('equal')
plt.show()

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1c)', '\n')
split = np.where(x==0)[0]
print(split)
oberschale = [[],[]]
unterschale = [[],[]]
for i in range(0,split[1]):
    oberschale[0].append(x[i])
    oberschale[1].append(y[i])
for i in range(split[1], len(x)):
    unterschale[0].append(x[i])
    unterschale[1].append(y[i])

plt.figure()
plt.subplot(121)
plt.plot(oberschale[0],oberschale[1],'r',label='Oberschale Flügelprofil')
plt.plot(unterschale[0],unterschale[1],'g',label='Unterschale Flügelprofil')
plt.xlabel('Horizontale Koordinaten')
plt.ylabel('Vertikale Koordinaten')
plt.legend(loc='upper right')
plt.axis('equal')
# plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1c)', '\n')
print(f'x_0={len(oberschale[0])}\nx_U={len(unterschale[0])}')
x_new = np.linspace(0,1,1000).tolist()

y_o = np.interp(x_new,oberschale[0][::-1],oberschale[1][::-1])
y_u = np.interp(x_new,unterschale[0],unterschale[1])

plt.subplot(122)
plt.fill_between(x_new,y_u,y_o)
plt.plot(x_new, y_o,'r',label='Oberschale Flügelprofil')
plt.plot(x_new, y_u,'g',label='Unterschale Flügelprofil')
plt.xlabel('Horizontale Koordinaten')
plt.ylabel('Vertikale Koordinaten')
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()















