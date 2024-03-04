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
#plt.tight_layout(pad=0.5)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1', '\n')
d = 0.25
m = 0.5
k = 1

print('\n\n\n', '\t\t\t Aufgabe a', '\n')
'''
    m*xpp + d*xp + k*x = 0
    => xpp + d/m*xp + k/m*x = 0
    => xpp = -d/m*xp - k/m*x
    
    mit y1 = x,  y2 = y1p = xp, y2p = y1pp = xpp
    => y2p = -d/m*y2 - k/m*y1
    =>  yp  = [y1p; y2p] = [y2; -d/m*y2 - k/m*y1]
    
    mit y1 = x[0],  y2 = x[1]
    =>  yp  = [y1p; y2p] = [x[1]; -d/m*x[1] - k/m*x[0]]
    
    in Python-Schreibweise:
    => yp  = [[y[1]], [-d/m*y[1] - k/m*y[0]]]
'''

print('\n\n\n', '\t\t\t Aufgabe b', '\n')
# ODE-Funktion
def u6_a1b(t,y,ma,b,c):
    y1p = y[1]
    y2p = (-b/ma * y[1] - c/m * y[0])
    return [y1p, y2p]

y0 = [2,0]
t = (0,20)
ts = 0.1

sol = solve_ivp(u6_a1b, t, y0, method='RK45', max_step=ts, args=(m,d,k))

plt.figure()
plt.plot(sol.t, sol.y[0], label=r'Auslenkung in $x~\downarrow$')
plt.plot(sol.t, sol.y[1], label='Geschwindigkeit')
plt.xlabel(r'Zeit $t$ in $s$')
plt.ylabel(r'Amplithude')
plt.legend(loc='best')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2', '\n')
'''
# FUNKTIONIERT NICHT, muss in Formelschreibweise
def u6_a2_not(t,x,M,B,C):  
    F = np.array([0,0,0,-5*np.cos(np.pi*t),0,0])
    np.transpose(F)
    x = np.append(x)
    A = np.array([[np.zeros(3), np.eye(3)],[-M.I*C, -M.I*B]])*x+F
    out = A.tolist()
    print(out)
    return out
'''
def u6_a2(t,x,m,b,c):
    x1, x1p, x2, x2p, x3, x3p = x[0], x[1], x[2], x[3], x[4], x[5]
    yp = [0, 0, 0, 0, 0, 0]

    yp[0] = x1p
    yp[1] = (-b * (3 * x1p - x2p) - c * (7 * x1 - 3 * x2) - 5 * np.cos(2 * t)) / m[0]
    yp[2] = x2p
    yp[3] = (-b * (-1 * x1p + 4 * x2p - 3 * x3p) - c * (-3 * x1 + 5 * x2 - 2 * x3)) / m[1]
    yp[4] = x3p
    yp[5] = (-b * (-3 * x2p + 3 * x3p) - c * (-2 * x2 + 2 * x3)) / m[2]
    return yp

m = [10, 20, 30]
b = 5
c = 20

anz_variablen = 3
t = (0,20)
ts = 0.1

x0 = np.zeros(2*anz_variablen).tolist()
sol = solve_ivp(u6_a2, t, x0, method='RK45', max_step=ts, args=(m, b, c))

plt.figure()
for n in range(anz_variablen):
    plt.plot(sol.t, sol.y[2*n], label=f'$x_{n+1}(t)$')
plt.xlabel('Zeit')
plt.ylabel('Weg')
plt.legend(loc='best')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 3', '\n')
L = 0.1
U0 = 9
R = 2
i0 = 0

def u6_a3(t,i):
    ip = (1/L) * (U0-R*i)
    return ip


t = np.linspace(0,1,50)

from scipy.integrate import odeint

i = odeint(u6_a3, i0, t)

# postprocessing
plt.plot(t,i,label='Current (Solver)')
plt.plot(t, (U0/R)*(1-np.exp(-(R*t)/L)), ':', label='Current (Analitical solution)')
plt.xlabel(r'time $t$')
plt.ylabel(r'current $I$')
plt.legend()
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 4', '\n')
'''
    2m*x1pp = -cx1 + c(x2-x1) + c(x3-x1)
     m*x2pp = -c(x2-x1) + F(t)
     m*x3pp = -c(x3-x1) 
'''

def u6_a4(t,x,m,c,f,omega):
    x1, x1p, x2, x2p, x3, x3p = x[0], x[1], x[2], x[3], x[4], x[5]
    yp = [0, 0, 0, 0, 0, 0]

    F = f*np.sin(omega*t)

    yp[0] = x1p
    yp[1] = (c * (-3*x1+x2+x3) + 0) / m[0]
    yp[2] = x2p
    yp[3] = (c * (x1-x2) + F) / m[1]
    yp[4] = x3p
    yp[5] = (c * (x1-x3) + 0) / m[2]
    return yp

F0 = 5
m=[2,1,1]
c=1000
omega=10

anz_variablen = 3
t = (0,100)
ts = 0.1

y0 = np.zeros(2*anz_variablen).tolist()
sol = solve_ivp(u6_a4, t, y0, method='RK45', max_step=ts, args=(m,c,F0,omega))

data = open(r'../src_extern_data/u6_a4_export.txt','w')
data.write('Datenexport - Übung 6 - Aufgabe 4\n')
data.write('Anregungsfrequenz:\t10\trad/s\n\n')
data.write('\tZeit\t\tx1(t)\t\tx1p(t)\t\tx2(t)\t\tx2p(t)\t\tx3(t)\t\tx3p(t)\n')
for n in range(len(sol.t)):
    data.write(f'{sol.t[n]:10.3}\t{sol.y[0][n]:10.3}\t{sol.y[1][n]:10.3}\t{sol.y[2][n]:10.3}\t{sol.y[3][n]:10.3}\t{sol.y[4][n]:10.3}\t{sol.y[5][n]:10.3}\n')
data.close()


plt.figure()
for n in range(anz_variablen):
    plt.plot(sol.t, sol.y[2*n], label=f'$x_{n+1}(t)$')
plt.xlabel('Zeit')
plt.ylabel('Auslenkung')
plt.legend(loc='best')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 5', '\n')
11
m = 1200
c = 400000
D = 0.2
b = 2*D*np.sqrt(c*m)
u0 = 0.05
v = 1 # Geschwindigkeit / m/s
L = 0.2 # Bodenwelle Länge / m
Omega = 2*np.pi*v/L # Berechnung der resultierenden Frequenz

def ode_func(t, x, m, b, c, u0, omega):
    x, xp = x[0], x[1]
    yp = [0, 0]

    yp[0] = xp
    yp[1] = -1/m * (c*x - c*u0*np.sin(omega*t) + b*xp - b*u0*omega*np.cos(omega*t))
    return yp

t=(0,10)
ts = 0.001

anz_variablen = 1
y0 = np.zeros(2*anz_variablen).tolist()
sol = solve_ivp(ode_func, t, y0, method='RK45', max_step=ts, args=(m, b, c, u0, omega))


# Exel Anlegen
file = open(r'../src_extern_data/u6_a5_export.csv','w')
file.write('Time; Amplitude\n')
for i in range(0,len(sol.t)):
    file.write(str(sol.t[i])+';'+str(sol.y[0][i])+'\n')
file.close()

plt.figure()
for n in range(anz_variablen):
    plt.plot(sol.t, sol.y[2*n], label=f'$x_{n+1}(t)$')
plt.xlabel('Zeit')
plt.ylabel('Auslenkung')
plt.legend(loc='best')
plt.grid()
plt.show()









