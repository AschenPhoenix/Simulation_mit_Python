#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 08
#
# _______________________________________________________________________
# --------- Main Bibliotheken --------------
import numpy as np
import math as mp
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import pytest
# --------- Weitere Bibliotheken --------------
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
# import opencv as cv2
# --------- Import anderer Dateien -------------
import Uebung_04_testfunk
# --------- Terminal vorbereiten ------------
# os.system('clear')
# os.system('cls')
# ================================== nächster Teil =================================
print(f'\n\n=====================\n||   Thema 1.0   ||\n=====================\n')
# ==================================================================================
polynom1 = np.array([1, 2, -9, -2, 5])  # Definition
x_min = -5
x_max = 3
x = np.linspace(x_min, x_max, 200)
y = np.polyval(polynom1, x)

plt.plot(x, y, 'r', label='Polynom 1', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend(loc='best')
plt.show()

# ================================== nächster Teil =================================
print(f'\n\n=====================\n||   Thema 2.0   ||\n=====================\n')
# ==================================================================================

Pol_roots = np.roots(polynom1)
y_0 = np.zeros(Pol_roots.shape)
plt.figure("Roots")
plt.plot(x, y, label='Polynom 1', linewidth=2)
plt.plot(Pol_roots, y_0, '*', label='Roots', linewidth=2)
plt.vlines(Pol_roots, -50, 175, 'g', ':')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend(loc='best')
plt.show()

# ================================== nächster Teil =================================
print(f'\n\n=====================\n||   Thema 2.0   ||\n=====================\n')
# ==================================================================================

plt.figure("Ableitung / Integration")
plt.plot(x, y, label='Polynom 1', linewidth=2)
plt.plot(Pol_roots, y_0, 'r*', label='Roots', linewidth=2)
plt.vlines(Pol_roots, -50, 170, 'g', ':')

poly_abl = np.polyder(polynom1)
poly_int = np.polyint(polynom1)
print(f'Polynom Ableitung: {poly_abl}')
print(f'Polynom Integration: {poly_int}')

poly_abl_plot = np.polyval(poly_abl, x)
poly_int_plot = np.polyval(poly_int, x)
plt.plot(x, poly_abl_plot, label='Polynom 1 - Ableitung', linewidth=2)
plt.plot(x, poly_int_plot, label='Polynom 1 - Integration', linewidth=2)

plt.text(-5.4, 200, 'np.polyval(Koeffizienten, x)', fontsize=12)

plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.legend(loc='best')
plt.show()

# ================================== nächster Teil =================================
print(f'\n\n=====================\n||   Thema 2.0   ||\n=====================\n')
# ==================================================================================
print (f'Vorlesung 8 Video weiter bei Minute 30')

# ================================== nächster Teil =================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
# ==================================================================================

# ========================== Ende =======================================
print("\n\n")
# =======================================================================
