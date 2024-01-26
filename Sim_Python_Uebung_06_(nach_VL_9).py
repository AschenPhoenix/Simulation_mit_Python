#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                       Uebung 06                                       #
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
print(f'\n\n=========================\n||  Aufgabe 1.0  ||\n=========================\n')
# =======================================================================================
'''
Differentialgleichung ist: [x1p; x2p] = [[0, 1]; [-k/m, -d/m]] * [x1; x2]
'''

d = 0.25
m = 0.5
k = 1
y0 = [2, 0]
t = np.arange(0, 20, 0.1)

def em_func(t,y):
    y1p = y[1]
    y2p = -k/m * y[0] - d/m * y[1]
    return y1p, y2p

sol = solve_ivp(em_func, t_span=(0, 20), y0=y0,  first_step=0.1, max_step=0.1)

plt.figure(1,figsize=(8, 3))
plt.plot(sol.t, sol.y[0], label='Massenschwinger')
plt.xlabel('Zeit t / s')
plt.ylabel('Auslenkung x / m')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.show()

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 2.0  ||\n=========================\n')
# =======================================================================================

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 3.0  ||\n=========================\n')
# =======================================================================================

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 4.0  ||\n=========================\n')
# =======================================================================================

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 5.0  ||\n=========================\n')
# =======================================================================================
'''
Bewegungsgleichung ist: m*xpp + b*xp + c*x = u0*sin(Omega*t) mit Omega abhängig von v0 wenn ich mich nicht täusche
Differentialgleichung ist: 
'''

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Weiter bei Aufgabe 0.0')