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
import scipy.integrate as s_int
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

def a1_func(t,y):
    y1p = y[1]
    y2p = -k/m * y[0] - d/m * y[1]
    return y1p, y2p

sol = solve_ivp(a1_func, t_span=(0, 20), y0=y0,  first_step=0.1, max_step=0.1)

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


def a2_func(t,y):
    y1p = y[1]
    y2p = 0.1 * (-15*y[1]+5*y[3] - 140*y[0]+60*y[2] - 5*np.cos(2*t))
    y3p = y[3]
    y4p = 0.05 * (5*y[1]-20*y[3]+15*y[5] + 60*y[0]-100*y[2]+40*y[4])
    y5p = y[5]
    y6p = (1/30)*(15*y[3]-15*y[5] + 40*y[2]-40*y[4])
    return y1p, y2p, y3p, y4p, y5p, y6p

y0 = [0, 0, 0, 0, 0, 0]
t = (0, 50)
ts = 0.1

sol = solve_ivp(a2_func, t, y0, method='RK45', max_step=ts)
styl = ['o-', '-', 1]

plt.figure()
plt.plot(sol.t, sol.y[0], styl[1], label='X1', linewidth=styl[2])
plt.plot(sol.t, sol.y[2], styl[1], label='X1', linewidth=styl[2])
plt.plot(sol.t, sol.y[4], styl[1], label='X1', linewidth=styl[2])
plt.xlabel('Auslenkung x')
plt.ylabel('Zeit t')
plt.grid()
plt.legend(loc='best')
plt.show()


# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 3.0  ||\n=========================\n')
# =======================================================================================
L = 0.1  # H
U0 = 9  # V
R = 2  # Ohm
I0 = 0
t = np.linspace(0, 1, num=50)

def a3_func(y, t):
    yp = (1/L) * (-y*R + U0)
    return yp

i = s_int.odeint(a3_func, I0, t)

print('odeint() Lösung A.3c: ', i[:, 0])
print('analytiasche Lösung A.3c: ', (U0/R)*(1-np.exp(-(R*t)/L)))
# postprocessing
plt.plot(t,i,label='Current (Solver)')
plt.plot(t, (U0/R)*(1-np.exp(-(R*t)/L)), ':', label='Current (Analitical solution)')
plt.xlabel(r'time $t$')
plt.ylabel(r'current $I$')
plt.legend(loc='best')
plt.grid()
plt.show()

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 4.0  ||\n=========================\n')
# =======================================================================================
def uebung_6_aufgabe_4(w):
    m = 1       # kg
    c = 1000    # N/m
    F0 = 5      # N
    Omega = w

    def a4_func(t, y):
        y1p = y[1]
        y2p = c / 2 * m * (y[2] - 3 * y[0] + y[4])
        y3p = y[3]
        y4p = c / m * (-y[2] + y[0]) + F0 / m * np.sin(Omega * t)
        y5p = y[5]
        y6p = c / m * (-y[4] + y[0])

        return [y1p, y2p, y3p, y4p, y5p, y6p]

    tspan = (0, 120)
    y0 = [0, 0, 0, 0, 0, 0]
    ts = 0.1

    sol = solve_ivp(a4_func, t_span=tspan, y0=y0, method='RK45', max_step=ts)

    # Plotten
    plt.figure()
    plt.title(f'Aufgabe 4 - Feder-Masse-System mit Anregungsfrequenz {w}rad/s')
    plt.plot(sol.t, sol.y[0], label='x1')
    plt.plot(sol.t, sol.y[2], label='x2')
    plt.plot(sol.t, sol.y[4], label='x3')
    plt.xlabel('Zeit in [s]')
    plt.ylabel('Auslenkung in [m]')
    plt.grid()
    plt.legend(loc='best')

    # Speichern in txt
    file = open(f'Uebung_6_Aufgabe_4.csv', 'w')
    file.write(f'')
    file.write(f'Frequenz: '+str(Omega)+'\n')
    file.write('Zeit'+';'+'X1'+';'+'X2'+';'+'X3'+';'+'\n')
    for i in range(0, len(sol.t)):
        file.write(str(sol.t[i])+';'+str(sol.y[0][i])+';'+str(sol.y[2][i])+';'+str(sol.y[4][i])+';'+'\n')
    file.close()

    file = open(f'Uebung_6_Aufgabe_4.csv', 'r+')
    print(file.read())
    file.close()

    plt.show()

uebung_6_aufgabe_4(10)

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 5.0  ||\n=========================\n')
# =======================================================================================

def uebung_6_aufgabe_5(y0=[0,0], v0=1, L=0.2):
    m = 1200
    c = 400000
    D = 0.2
    b = 2*D*np.sqrt(c*m)
    u0 = 0.05
    t = (0, 10)
    ts = 0.001

    def a5_func(t,y):
        Omega = (2*np.pi*v0)/L

        y1p = y[1]
        y2p = c/m * (u0*np.sin(Omega*t)-y[0]) + b/m * (u0*Omega*np.cos(Omega*t)-y[1])

        return [y1p, y2p]

    sol = solve_ivp(a5_func, t, y0, method='RK45', max_step=ts)

    plt.figure(f'Übung 6 - Aufgabe 5')
    plt.subplot(121)
    plt.title(f'Auslenkung-Weg-Diagramm')
    plt.plot(sol.t, sol.y[0], label='y')
    plt.xlabel('Zeit in [s]')
    plt.ylabel('Auslenkung in [m]')
    plt.grid()
    plt.legend(loc='best')

    plt.subplot(122)
    plt.title(f'Geschwindigkeit-Weg-Diagramm')
    plt.plot(sol.t, sol.y[1], label='yp')
    plt.xlabel('Zeit in [s]')
    plt.ylabel('Vertikal-Geschwindigkeit in [m/s]')
    plt.grid()
    plt.legend(loc='best')

    # Speichern
    cut = ';'
    file = open('Uebung_6_Aufgabe_5.xlsx', 'w')
    file.write(f'Anfangsbedingungen: '+cut+str(y0)+'\n')
    file.write(f'Fahrgeschwindigkeit: ' + cut + str(v0)+'\n')
    file.write(f'Bahn-Wellenlänge: ' + cut + str(L)+'\n')
    file.write('\n')
    file.write('\n')
    file.write('Zeit' + cut + 'Auslenkung' + cut + 'Vertikalgeschwindigkeit'+'\n')
    file.write('s'+cut+'m'+cut+'m/s'+'\n')
    for i in range(0,len(sol.t)):
        file.write(str(sol.y[0][i])+cut+str(sol.y[1][i])+'\n')
    file.close()

    file = open(f'Uebung_6_Aufgabe_5.xlsx', 'r+')
    print(file.read())
    file.close()

    plt.show()
# ______________________
uebung_6_aufgabe_5()

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Weiter bei Aufgabe 0.0')