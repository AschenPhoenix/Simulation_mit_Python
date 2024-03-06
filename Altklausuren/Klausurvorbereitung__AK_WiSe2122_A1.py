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
print('\n\n\n', '\t\t\t Aufgabe 1a', '\n')

path = r'../Altklausuren/WS2122/experimentalData.csv'
dehnung = []
kraft = []
with open(path) as csv_data:
    csv_read = csv.reader(csv_data, delimiter=',')
    headers = next(csv_read)
    for row in csv_read:
        dehnung.append(float(row[0]))
        kraft.append(float(row[1]))
csv_data.close()
print(len(dehnung),dehnung)
print(len(kraft),kraft)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1b', '\n')

p, res, _, _, _ = np.polyfit(dehnung, kraft, 4, full=True)
e = float(res/(len(kraft)*max(kraft)))
print(f'\n\t \"Das Polynom 4.Ordnung besitzt einen Fehler von {e:5.2}%\"\n')

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1c', '\n')

dehn = np.linspace(min(dehnung), max(dehnung), 100)
F = np.polyval(p,dehn)

plt.figure()
plt.plot(dehnung, kraft, color='gray', label='Messdaten')
plt.plot(dehn, F, color='k', label='gefittetes Modell')
plt.legend(loc='best')
plt.xlabel('Dehnung in [1]')
plt.ylabel('Kraft in [uN]')
plt.xlim([0,0.6])
plt.grid()
plt.show()













