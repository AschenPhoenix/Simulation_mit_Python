# |==============| Bibliotheken |==============|
#                     region
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

# |~~~~~~~~~~~~| Main Bibliotheken |~~~~~~~~~~~|
import numpy as np
import math as mth
import scipy as sc
import matplotlib.pyplot as plt
import matplotlib as mplt
import scipy.optimize
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
print('\n\n\n', '\t\t\t Aufgabe 1a)', '\n')
'''
0 = 3*t/l - 4*(t/l)**3 - rd
'''
def tl_ratio(x,rd):
    return (3*x - 4*x**3 - rd)

rd = 0.05
l = 22.5
x0 = 0.1
x = scipy.optimize.newton(tl_ratio, x0, args=(rd,))
print(f'Wandstärke ist t={x*l}')

def wall_thickness(rd,l):
    X0 = 0.1
    x = scipy.optimize.newton(tl_ratio, X0, args=(rd,))

    t=[]
    for k in l: t.append(x*k)
    return t

rel_dichten = (0.25, 0.5, 0.75, 1.0)
wand = []
plt.figure()
for n,rd in enumerate(rel_dichten):
    l = np.linspace(5,40,200)
    wand.append(wall_thickness(rd,l))
    print(wand[n])
    plt.plot(l,wand[-1], label=f'rd={rd}')

plt.xlabel('Einheitszellenlänge l')
plt.ylabel('Wandstärke t')
plt.xlim([5,40])
plt.grid()
plt.legend(loc='best')
plt.show()


















