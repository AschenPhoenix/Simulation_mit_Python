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
print(f'\n\n===========================\n||  Thema 1 ||\n============================\n')
# =======================================================================================

print(f'========||  explites Eulerverfahren ||========\n')
t1 = np.arange(0, 5, 0.01)
y1 = 2.5*t1**2

plt.figure(1)
plt.plot(t1,y1)
plt.show()

# numerische Lösung mit explizitem Euler-Verfahren
h = 0.5
t2 = np.arange(0, 5, h)
y2 = np.zeros(len(t2))

for i in range(1, len(t2)):
    y2[i] = y2[i-1] + h*5*t2[i-1]

plt.figure(1)
plt.plot(t1, y1)
plt.plot(t2, y2, 'o-')
plt.grid()
plt.show()

# ====================================== nächster Teil ==================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
# =======================================================================================
t = np.arange(0.0, 5.0, h)

plt.figure()
plt1 = plt.subplot(121)
y_ex = np.zeros(len(t))
y_im = np.zeros(len(t))
for h in [0.5, 0.2, 0.05, 0.02, 0.001]:
    y_ex[0] = 1
    for i in range(1,len(t)):
        y_ex[i] = y_ex[i - 1] + h * (-5*(y_ex[i-1]-2))
    plt1.plot(t, y_ex, 'o-', linewidth=2, label=f'h={h} - explizit Euler')

y_ana = 2 - np.exp(-5 * t)
plt1.plot(t, y_ana, 'b', linewidth=2, label='Analytische Lösung')
plt1.set_title('Explizite Eulerverfahren')
plt1.legend(loc='best')
plt1.grid()

plt2 = plt.subplot(122)
for h in [0.5, 0.2, 0.05, 0.02, 0.001]:
    y_im[0] = 1
    for i in range(1,len(t)):
        y_im[i] = (y_im[i-1]+10*h)/(1+5*h)
    plt2.plot(t, y_im, 'o-', linewidth=2, label=f'h={h} - implizit Euler')

y_ana = 2 - np.exp(-5 * t)
plt2.plot(t, y_ana, 'b', linewidth=2, label='Analytische Lösung')
plt2.set_title('Implizite Eulerverfahren')
plt2.legend(loc='best')
plt2.grid()
plt.show()

# ======================================= nächster Teil =================================
print(f'\n\n===========================\n||  Thema 2 ||\n============================\n')
# =======================================================================================
print(f"Vorlesung`s Video weiter bei 00:16:00")

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f"Vorlesung`s Video weiter bei 00:00:00")
