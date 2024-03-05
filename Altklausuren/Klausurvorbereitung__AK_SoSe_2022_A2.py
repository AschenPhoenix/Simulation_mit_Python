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
print('\n\n\n', '\t\t\t Aufgabe 2a)', '\n')

def ode_func(t, x, m, d, c, u=0):
    x1, x1p, x2, x2p = x[0], x[1], x[2], x[3]

    if t<=300: c3=10000
    else: c3=0

    if (t%100)>=50: u = 0.1

    yp = np.zeros(len(x)).tolist()
    yp[0] = x1p
    yp[1] = -1/m[0] * ((d[0]+d[1])*x1p - d[1]*x2p + (c[0]+c[1]+c3)*x1 - (c[1]+c3)*x2) + c[0]/m[0]*u
    yp[2] = x2p
    yp[3] = -1/m[1] * (-d[1]*x1p + d[1]*x2p - (c[1]+c3)*x1 + (c[1]+c3)*x2)
    
    return yp

m=(1,0.01)
d=(0.001,0.005)
c1=10
c2=c1*m[1]/m[0]
c=(c1,c2)

t=(0,600)
ts = 0.01

anz_variablen = 2
y0 = np.zeros(2*anz_variablen).tolist()
sol = solve_ivp(ode_func, t, y0, method='RK45', max_step=ts,  args=(m, d, c))

plt.figure()
plt.tight_layout(pad=0.5)

plt.subplot(211)
plt.plot(sol.t, sol.y[0], label=f'$x_{1}(t)$')
plt.xlabel('Zeit')
plt.ylabel(f'Auslenkung $x_1$')
plt.legend(loc='best')
plt.grid()

plt.subplot(212)
plt.plot(sol.t, sol.y[2], label=f'$x_{2}(t)$')
plt.xlabel('Zeit')
plt.ylabel(f'Auslenkung $x_2$')
plt.legend(loc='best')
plt.grid()
plt.show()
















