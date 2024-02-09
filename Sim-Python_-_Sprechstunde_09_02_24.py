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
#########################################################################################

# ======================================= nächster Teil =================================
print(f'\n\n=====================\n||  SoSe2023 Aufgabe 2.0  ||\n=====================\n')
# =======================================================================================
H0 = 100
F0 = 20
t_span = (0, 100)
a = 0.03
b = 0.001
c = 0.1
d = 0.002

y0 = [H0, F0]
t_eval = np.linspace(0, t_span[1],100)

# Aufgabe 2a
def ode_rauber_beute(t, y, a, b, c, d):
    H, F = y
    Hp = a*H-b*F*H
    Fp = -c*F + d*H*F
    return[Hp, Fp]


sol = solve_ivp(ode_rauber_beute, t_span, y0, method='Radau', t_eval=t_eval, args=(a, b, c, d))
dH, dF = ode_rauber_beute(sol.t, sol.y, a, b, c, d)

# ______________________________________
# Aufgabe 2b
plt.figure()
plt.subplot(211)
plt.plot(sol.t, sol.y[0], 'b-', label='Hasenpopulation')
plt.plot(sol.t, sol.y[1], 'r-', label='Fuchspopulation')
plt.xlabel('Zeit in Jahren')
plt.ylabel('Populationsgröße')
plt.grid()
plt.legend()

plt.subplot(212)
plt.plot(sol.t, dH, 'b--', label='Hasenpopulation')
plt.plot(sol.t, dF, 'r--', label='Fuchspopulation')
plt.xlabel('Zeit in Jahren')
plt.ylabel('Änderung der Population')
plt.grid()
plt.legend()

# plt.show()


# ______________________________________
# Aufgabe 2c

a_span = np.arange(0.01, 0.11, 0.01)
t_new = (0, 15)
t_eval = np.linspace(0, t_new[1],100)
solutions = []
H_final = []
F_final = []

for a in a_span:
    sol_new = solve_ivp(ode_rauber_beute, t_new, y0, method='Radau', t_eval=t_eval, args=(a, b, c, d))
    solutions.append(sol_new)
    H_final.append(sol_new.y[0][-1])
    F_final.append(sol_new.y[1][-1])


# ______________________________________
# Aufgabe 2d
plt.figure('Aufgabe 2d')
plt.plot(a_span, H_final, 'bx--', label='Endwerte der Hasenpopulation')
plt.plot(a_span, F_final, 'rx--', label='Endwerte der Fuchspopulation')
plt.xlabel('Wachstumsrate der Hasen')
plt.ylabel('Endpopulationsgröße nach 15 Jahren')
plt.grid()
plt.legend()

plt.show()


# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f"Vorlesung`s Video weiter bei 00:00:00")
