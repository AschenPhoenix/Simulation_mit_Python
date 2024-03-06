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

def ode_func(t, x, m, b, c):
    x1, x1p, x2, x2p = x[0], x[1], x[2], x[3]

    yp = np.zeros(len(x)).tolist()
    yp[0] = x1p
    yp[1] = 1/m[0] * (c[1]*x2 - c[1]*x1 - c[0]*x1 - b[0]*x1p)
    yp[2] = x2p
    yp[3] = 1/m[1] * (-b[1]*x2p - c[1]*x2 + c[1]*x1)
    return yp

m = [3, 1]
b = [0.01, 0.05]
c = [1, 0.1]

t=(0,250)
ts = 0.1
y0=[0,0,5,0]
sol = solve_ivp(ode_func, t, y0, method='RK45', max_step=ts,  args=(m, b, c))

fc2=[]
s2=[]
for i in range(len(sol.t)):
    s2.append(float(sol.y[2][i] - sol.y[0][i]))
    fc2.append(c[1]*s2[i])

plt.figure()
plt.subplot(121)
plt.plot(sol.t, s2)
plt.xlabel('Zeit')
plt.ylabel(f'Streckung der Feder 2')
plt.legend(loc='best')
plt.grid()

plt.subplot(122)
plt.plot(sol.t, fc2)
plt.xlabel('Zeit')
plt.ylabel(f'Federkraft der Feder 2')
plt.legend(loc='best')
plt.grid()
plt.show()

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2b', '\n')
from kennlinien_approx import kennlinie

path = r'../Altklausuren/SS2021/federkennlinie_optimierte_parameter.txt'
para = []
with open(path) as csv_data:
    csv_read = csv.reader(csv_data, delimiter=';')
    for row in csv_read:
        para.append(float(row[1]))
csv_data.close()
print(para)

curve_opt = []
for i in range(len(sol.t)):
    curve_opt.append(kennlinie(s2[i], para[0], para[1]))

plt.figure()
plt.subplot(121)
plt.plot(sol.t, s2)
plt.xlabel('Zeit')
plt.ylabel(f'Streckung der Feder 2')
plt.legend(loc='best')
plt.grid()

plt.subplot(122)
plt.plot(sol.t, fc2, label = r'$F_{c2} aus 2a')
plt.plot(sol.t, curve_opt, label = r'$F_{c2} aus 2b')
plt.xlabel('Zeit')
plt.ylabel(f'Federkraft der Feder 2')
plt.legend(loc='best')
plt.grid()
plt.show()






