#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                      Vorlesung 10                                     #
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
from matplotlib import colormaps as cm
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
print(f'\n\n=====================||  Thema: Approximation partieller Differentialgleichungen  ||=====================\n')
# =======================================================================================

def f(x):
    return -2*x**2+3*x-40

def fd(x):
    return -4*x+3

def fdT(x,h):
    return (f(x+h)-f(x))/h

# ------------------------------------------------------------------------------------------------
x0 = 5
h = np.array([3.0, 1.5, 0.1, 0.01, 0.001])
# ------------------------------------------------------------------------------------------------
fi = fdT(x0,h)   # finite differenzen Approximation
fa = fd(x0)      # algebraische Lösung

print(f'aprox. : {fi}')
print(f'alg. : {fa}')
num_error = np.abs(fi-fa)
print(f'Fehler der Approximation: {num_error}')
# ------------------------------------------------------------------------------------------------
plt.loglog(h, num_error, '.-', label='Approximationsfehler')
plt.xlabel('Schrittweite')
plt.ylabel('Numerischer Fehler')
plt.title('Fehler der Approximation')
plt.legend()
plt.grid()
plt.show()
# ====================================== nächster Teil ==================================
print(f'\n\n=======================||   Thema: 2D-Wärmeleitungsgleichung   ||=======================\n')
# =======================================================================================
def handle_close(evt):
    print('Close Figure!')
    quit()

# ------------------------------------------------------------------------------------------------
# Materialdefinition
D = 10.

# Plattengröße
w = he = 10.

# Schrittweite dx = dy = h
h = 0.5

# Anzahl der schritte im Raum
nx, ny = int(w/h), int(he/h)
# meshgrid erstellen
X, Y = np.meshgrid(np.linspace(0, w, nx), np.linspace(0, he, ny))

# Timestep
dt = h**2/(4*D)
# dt = h**2/(4*D)*2 # Es entstehen numerische Instabilitäten,
#                     die zu Schwingungen in der Berechnung und extrem hohen mathematischen Fehlern führen
t = 2

# ------------------------------------------------------------------------------------------------
# Anfangsbedingungen
T_cool, T_hot = 10., 150.
u = np.zeros((nx, ny))
u0 = T_hot*np.ones((nx, ny))

# X-Achse als Parabel
# u0(x,0)
x = np.linspace(0, w, nx)
u[:, 0] = -((4*T_hot)/w**2)*x**2 + ((4*T_hot)/w)*x
# u0[:, 0] = T_cool

# u0(x,nx-1)
u0[:, nx-1] = T_cool

# u0(0,y)
u0[0, :] = T_cool
# u0(ny-1,y)
u0[ny-1, :] = T_cool

u=u0.T
# ------------------------------------------------------------------------------------------------
# Plotten
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('temperatur')
ax.set_zlim3d(0.0, 200)
wframe = None
# ------------------------------------------------------------------------------------------------

# u[i,j] = (1-(4*dt*D)/dx**2) * u0[i,j] +(dt*D)/dx**2 * (u0[i,j-1] + u0[i-1,j] + u0[i+1,j] + ue0[i,j+1])
for ti in np.linspace(0,t,int(t/dt)):
    if wframe:
        #ax.cla()
        ax.collections.remove(wframe)
        textvar.set_visible(False)
    for i in range(1, len(X)-1):
        for j in range(1, len(Y)-1):
            u[i,j] = (1-(4*dt*D)/h**2) * u0[i,j] + (dt*D)/h**2 * (u0[i,j-1] + u0[i-1,j] + u0[i+1,j] + u0[i,j+1])
    wframe = ax.plot_surface(X, Y, u)  #, cmap=cm.jet) , cma p=cm.coolwarm)
    textvar = ax.text(0, 10,  200, f't={ti:.4}s')
    u0 = u.copy()
    plt.pause(0.1)
    fig.canvas.mpl_connect('close_event', handle_close)
plt.show()

print('Am Ende dieser Vorlesung gibt es noch eine Übung, die bearbeitet werden  und sollte!')
# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f"Vorlesung`s Video weiter bei 00:00:00")
