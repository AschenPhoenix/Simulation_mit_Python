#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                       Uebung 05                                       #
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
import copy
from sympy import true
from scipy.interpolate import interp1d
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
print(f'\n\n=========================\n||  Aufgabe 0.0  ||\n=========================\n')
# =======================================================================================

auslenkung = [0, 1, 2, 3, 4, 5]
kraft = [0, 940, 1554, 2069, 2438, 2509]

x = np.linspace(0, 5, 200)
p_deg1 = np.polyfit(auslenkung, kraft, 1)
p_deg2 = np.polyfit(auslenkung, kraft, 2)

y_deg1 = np.polyval(p_deg1, x)
y_deg2 = np.polyval(p_deg2, x)

kraft_bei_federweg = np.polyval(p_deg2, 3.5)
y_min = min(y_deg2)
y_max = max(y_deg2)

plt.figure('Aufgabe 0')
plt.plot(auslenkung, kraft, 'y*', label='Originalwerte', linewidth=3)
plt.plot(x, y_deg1, 'b', label='Approximation als lineares Polynom', linewidth=2)
plt.plot(x, y_deg2, 'g', label='Approximation als quadratisches Polynom', linewidth=2)
plt.hlines(kraft_bei_federweg, x[0], x[-1], 'r', label=f'Kraft von {kraft_bei_federweg:.3f}N\nbei Federweg von 3.5 cm')
plt.vlines(3.5, y_min, y_max, 'r')
plt.xlabel('Auslenkung in [cm]')
plt.ylabel('Kraft in [N]')
plt.grid()
plt.legend(loc='best')
plt.show()


# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 1.0  ||\n=========================\n')
# =======================================================================================
t_be = [0, 2, 4, 6, 8, 10]
s_be = [0, 20, 80, 180, 320, 500]
t_br = [10, 20, 30, 40, 50, 60]
s_br = [500, 1400, 2100, 2600, 2900, 3000]

p_s_be = np.polyfit(t_be, s_be, 2)
p_s_br = np.polyfit(t_br, s_br, 2)
p_v_be = np.polyder(p_s_be)
p_v_br = np.polyder(p_s_br)
v_be = np.polyval(p_v_be, t_be)
v_br = np.polyval(p_v_br, t_br)

plt.figure('Aufgabe 1')
plt.subplot(211)
plt.title('v-t-Diagramm')
plt.plot(t_be, v_be, 'g', label='Geschwindigkeit beim Beschleunigen', linewidth=2)
plt.plot(t_br, v_br, 'r', label='Geschwindigkeit beim Bremsen', linewidth=2)
plt.xlabel('Zeit in [s]')
plt.ylabel('Geschwindigkeit in [m/s]')
plt.grid()
plt.legend(loc='best')

plt.subplot(212)
plt.title('s-t-Diagramm')
plt.plot(t_be, s_be, 'g', label='Weg beim Beschleunigen', linewidth=2)
plt.plot(t_br, s_br, 'r', label='Weg beim Bremsen', linewidth=2)
plt.xlabel('Zeit in [s]')
plt.ylabel('Weg in [m]')
plt.grid()
plt.legend(loc='best')

plt.tight_layout(pad=0.5)
plt.show()

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Weiter bei Aufgabe 0.0')
