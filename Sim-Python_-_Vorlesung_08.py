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
print("\n\n\n")
# ======================================== Teil 01 =================================
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
plt.legend('best')
plt.show()

# ======================================== Teil 02 =================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
# ==================================================================================

# ========================== Ende =======================================
print("\n\n")
# =======================================================================
