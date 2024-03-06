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
print('\n\n\n', '\t\t\t Aufgabe 2a', '\n')

def ode_func(t, x, A1, E1, m, n, Qm, R, cp, Qsp):
    a, T, = x[0], x[1]
    ap = A1*np.exp(-E1/(R*T)) * (a**m) * (1-a)**n
    Tp = 1/cp * (Qm*ap+Qsp)
    return [ap, Tp]


A1 = 400
E1 = 18700
m = 1.5
n = 1.7
Qm = 84000
R = 8.3
cp = 1100
Qsp = -142

t = (0, 300)
ts = 0.1
y0 = [0.01, 280]
sol = solve_ivp(ode_func, t, y0, method='RK23', max_step=ts, args=(A1, E1, m, n, Qm, R, cp, Qsp))


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2b', '\n')

plt.figure()
plt.subplot(311)
plt.plot(sol.t, sol.y[1], 'r')
plt.xlabel('Zeit t in [s]')
plt.ylabel('Temperatur in [K]')
plt.grid()


plt.subplot(312)
plt.plot( sol.t, sol.y[0], 'b')
plt.xlabel('Zeit t in [s]')
plt.ylabel(r'Aushärtegrad $\alpha$ in [-]')
plt.grid()

ap = []
for i in range(len(sol.t)):
    ap.append(ode_func(sol.t[i], [sol.y[0][i], sol.y[1][i]], A1, E1, m, n, Qm, R, cp, Qsp)[0])

plt.subplot(313)
plt.plot(sol.t, ap, 'g')
plt.xlabel('Zeit t in [s]')
plt.ylabel(r'Aushärtungsrate d$\alpha/dt$ in [$1/K$]')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2c', '\n')
A1 = 400
E1 = 18700
m = 1.5
n = 1.7
Qm = 84000
R = 8.3
cp = 1100
Qsp = -142

fin = []
T_start = np.linspace(270, 350, 9)
for T0 in T_start:
    t = (0, 1000)
    ts = 1
    y0 = [0.01, T0]
    solc = solve_ivp(ode_func, t, y0, method='RK23', max_step=ts, args=(A1, E1, m, n, Qm, R, cp, Qsp))
    a = solc.y[0]
    k = min(np.where(a>0.99)[0])
    fin.append(solc.t[k])

plt.figure()
plt.plot(T_start, fin, 'x--')
plt.xlabel('Starttemperatur')
plt.ylabel('Zeit bis zum vollständigen Aushärten')
plt.grid()
plt.show()











