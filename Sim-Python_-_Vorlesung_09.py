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


plt.figure()
plt1 = plt.subplot(121)
for h in [0.001, 0.02, 0.05, 0.2, 0.5]:
    t = np.arange(0.0, 5.0, h)
    y_ex = np.zeros(len(t))
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
for h in [0.001, 0.02, 0.5, 0.2, 0.1]:
    t = np.arange(0.0, 5.0, h)
    y_im = np.zeros(len(t))
    y_im[0] = 1
    for i in range(1, len(t)):
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
# t = np.arange(0.0, 5.0, 0.1)


def func(t,y):
    yp = -5*(y-2)
    return yp


sol = solve_ivp(func, t_span=(0, 5), y0=[1])
plt.plot(t, y_ana, 'o-', linewidth=2, label='Analytische Lösung')
plt.plot(t, y_im, 'o-', linewidth=2, label=f'h={h} - implizit Euler')
plt.plot(sol.t, sol.y[0], 'o-', label='solve_ivp')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# ======================================= nächster Teil =================================
print(f'\n\n===========================\n||  Thema 3 ||\n============================\n')
# =======================================================================================
print(f'===== System gekoppelter Differentialgleichungen =====')
t = np.arange(0.0, 10.0, 0.5)


def funk(t, y):
    y1p = -80.69*y[0]+119.4*y[1]
    y2p = 79.6*y[0]-120.4*y[1]
    return [y1p, y2p]


sol45 = solve_ivp(funk, t_span=(0,10), y0=[0,1], method="RK45")

plt.figure()
plt.subplot(221)
plt.title("RK45 y_1")
plt.plot(sol45.t, sol45.y[0,:], "o-", label="y1")
plt.legend()

plt.subplot(222)
plt.title("RK45 y_2")
plt.plot(sol45.t, sol45.y[1,:], "o-", label="y2")
plt.legend()

solRad = solve_ivp(funk, t_span=(0,10), y0=[0,1], method='Radau')

plt.subplot(223)
plt.title("Radau y_1")
plt.plot(solRad.t, solRad.y[0,:], "o-", label="y1")
plt.legend()

plt.subplot(224)
plt.title("Radau y_2")
plt.plot(solRad.t, solRad.y[1,:], "o-", label="y2")
plt.legend()

plt.show()



# ====================================== nächster Teil ==================================
print(f'\n\n=======================\n||   Bsp Aufgabe 2   ||\n=======================\n')
# =======================================================================================
print(f'===== mathematisches Pendel =====')
print(f'Code als Bild in Dateien, gut zum üben!')

print(f'\n\n===== Zweimassenschwinger =====')
def massenfunc(t, y):
    y1p = y[1]
    y2p = -10*y[1]+2.5*y[3]-25*y[0]+5*y[2]+np.sin(3*t)
    y3p = y[3]
    y4p = 0.5*y[1]-0.5*y[3]+y[0]-y[2]+0.5*np.cos(5*t)
    return[y1p,y2p,y3p,y4p]

# Anfangsbedingungen
y0 = [1, 0, -1,  0]
t = (0, 40)

sol = solve_ivp(massenfunc, t, y0, max_step=0.1)

plt.figure(1,figsize=(8,3))
plt.plot(sol.t, sol.y[0], label='m1')
plt.plot(sol.t, sol.y[2], label='m2')
plt.xlabel('Zeit / s')
plt.ylabel('Auslenkung / m')
plt.legend(loc='best')
plt.tight_layout()
plt.show()


print(f'\n\n===== elektrischer Schwingkreis =====')

print(f'\n\n===== Duffing-Oszillator =====')
print(f'Übungsaufgabe (Video ab 00:52:40), von mir noch NICHT bearbeitet!')
print(f'Die Lösung dieser Aufgabe ist in VL12 bei 00:09:26 gezeigt.')

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f"Vorlesung`s Video weiter bei 00:00:00")
