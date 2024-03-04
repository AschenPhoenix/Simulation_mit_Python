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

def population(t,p, a, b, c, d):
    """
    Funktion zur Berechnung der Population der Hasen und Füchse
    :param: t, p, a, b, c, d
    """
    Hp = a*p[0]-b*p[1]*p[0]
    Fp = -c*p[1]+d*p[1]*p[0]
    return [Hp, Fp]

# Aufruf der Populationsfunktion
H0 = 100
F0 = 20
a=0.03
b=0.001
c=0.1
d=0.002

t = (0,100)
t_eval = np.arange(0,101,1)
pop = solve_ivp(population, t, [H0,F0], t_eval=t_eval, method='Radau', args=(a, b, c, d))
[Hp,Fp] = population(pop.t, pop.y, a, b, c, d)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2b)', '\n')
plt.figure()
plt.subplot(311)
plt.plot(pop.t, pop.y[0], 'b', label=f'Hasenpopulation')
plt.plot(pop.t, pop.y[1], 'r', label=f'Fuchspopulation')
plt.xlabel('Jahre')
plt.ylabel('Population')
plt.legend(loc='best')
plt.grid()

plt.subplot(312)
plt.plot(pop.t, Hp, 'b--', label=f'Änderung der Hasenpopulation')
plt.plot(pop.t, Fp, 'r--', label=f'Änderung der Fuchspopulation')
plt.xlabel('Jahre')
plt.ylabel('Populationsänderung')
plt.legend(loc='best')
plt.grid()
#plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2c)', '\n')

einfluss= [[],[],[]]
for a in np.linspace(0.01,0.1, 10):
    sol = solve_ivp(population, (0,15), [H0,F0], method='Radau', args=(a, 0.001, 0.1, 0.002))
    einfluss[0].append(a)
    einfluss[1].append(sol.y[0][-1])
    einfluss[2].append(sol.y[1][-1])

plt.subplot(313)
plt.plot(einfluss[0], einfluss[1], 'bx--', label=f'Hasenpopulation abhängig von a')
plt.plot(einfluss[0], einfluss[2], 'rx--', label=f'Fuchspopulation abhängig von a')
plt.xlabel('Wachstumsrate a')
plt.ylabel('Population')
plt.legend(loc='best')
plt.xlim([0.01,0.1])
plt.grid()
plt.show()












