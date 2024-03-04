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

def ode_func(t, x, f, L, U, R, C):
    i, ip, = x[0], x[1]
    yp = np.zeros(len(x)).tolist()
    yp[0] = ip
    yp[1] = 1/L * (2*np.pi*f*U*np.sin(2*np.pi*f*t) - R*ip - i/C)
    return yp

t = (0,0.3)
f=10
U=1
R=1
C=0.001
L=0.01

plt.figure()
for n in range(1):
    y0 = (0, 0)
    sol = solve_ivp(ode_func, t, y0, t_eval=np.linspace(0,0.3,121), method='RK45', args=(f, L, U, R, C))
    plt.plot(sol.t, sol.y[n], label=f'I(f) bei f={f}HZ')
# print(sol.t[80])
plt.xlabel('Zeit in [s]')
plt.ylabel('Strom I in [A]')
plt.legend(loc='best')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2b', '\n')
t = (0,0.3)
para = (1, 1, 0.001, 0.01)
U=1
R=1
C=0.001
L=0.01

plt.figure()
I = []
f=[]
for n,F in enumerate(np.logspace(10,100,100)):
    y0 = (0, 0)
    f.append(f'f{n}')
    f[n] = solve_ivp(ode_func, t, y0, method='RK45',t_eval=np.linspace(0,0.3,121), args=(F, L, U, R, C))
    plt.plot(f[n].t, f[n].y[0], label=f'I(f) bei f={F}HZ')
plt.xlabel('Zeit in [s]')
plt.ylabel('Strom I in [A]')
plt.legend(loc='best')
plt.grid()
plt.show()












