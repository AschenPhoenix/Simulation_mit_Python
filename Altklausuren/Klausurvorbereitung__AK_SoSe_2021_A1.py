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

path = r'../Altklausuren/SS2021/federkennlinie_klausur.csv'
csv_weg = []
csv_kraft = []
with open(path) as csv_data:
    csv_read = csv.reader(csv_data, delimiter=' ')
    for row in csv_read:
        csv_weg.append(float(row[0]))
        csv_kraft.append(float(row[1]))
csv_data.close()

plt.figure()
plt.plot(csv_weg, csv_kraft, 'gx')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1b', '\n')
from scipy.optimize import curve_fit
def kennlinie(x, a=1, b=1):
    return (x/a * np.abs(np.tanh(x/b)))

kenn_opt = curve_fit(kennlinie, csv_weg, csv_kraft, p0=[1,1])[0]
print(kenn_opt)
x=np.linspace(-10,10,1000)
curve_opt = kennlinie(x, kenn_opt[0], kenn_opt[1])
plt.figure()
plt.plot(csv_weg, csv_kraft, 'gx', label='Messwerte')
plt.plot(x, curve_opt, 'k--', label='optimierte Lösung')
plt.text(-10,1, f'a = {kenn_opt[0]:8.5}\nb = {kenn_opt[1]:8.5}')
plt.xlabel('Weg')
plt.ylabel('Kraft')
plt.legend(loc='lower right')
plt.grid()
plt.show()

data = open(r'../Altklausuren/SS2021/federkennlinie_optimierte_parameter.txt','w')
data.write(f'Optimaler Parameter a: ;{kenn_opt[0]}\n')
data.write(f'Optimaler Parameter b: ;{kenn_opt[1]}\n')
data.close()











