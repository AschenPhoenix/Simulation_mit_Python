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

print('\n\n\n#########################################################################################')
print('\t\t\t Aufgabe 1a', '\n')
#path = r'C:\Users\User\OneDrive\Uni und Verbindung\Uni und aktuelles Semester\Aktuelles Semester\WiSe 2324 - Simulation technischer Systeme mit Python\Eigene Programme\Simulation_mit_Python\Altklausuren\SS2023\od_deaths_usa.csv'
path = r'..\Altklausuren\SS2023\od_deaths_usa.csv'
data_a1 = []
with open(path) as csv_data:
    csv_read = csv.reader(csv_data, delimiter='\t')
    for row in csv_read:
        data_a1.append(row)
    for n in range(1,len(data_a1)):
        for m in range(3):
            data_a1[n][m] = int(data_a1[n][m])
csv_data.close()

year = []
total = []
fentanyl = []
names = [data_a1[0][0], data_a1[0][1], data_a1[0][2]]
for k in range(1,len(data_a1)):
    year.append(data_a1[k][0])
    total.append(data_a1[k][1])
    fentanyl.append(data_a1[k][2])
print(year)
print(total)
od_death_usa = {names[0]:year, names[1]:total, names[2]:fentanyl}
for key, value in od_death_usa.items():
    print(key, f":\t", value)


print('\n\n\n#########################################################################################')
print('\t\t\t Aufgabe 1b', '\n')
plt.figure('Aufgabe 1b)')
plt.plot(od_death_usa[names[0]], od_death_usa[names[1]], 'bo-', label=f'{names[1]} overdose')
plt.plot(od_death_usa[names[0]], od_death_usa[names[2]], 'ro-', label=f'{names[2]} overdose')
plt.xlabel('Years (1990 to 2020)')
plt.ylabel('Number of Deaths')
plt.legend(loc='best')
plt.grid()
plt.show()


print('\n\n\n#########################################################################################')
print('\t\t\t Aufgabe 1c', '\n')
from scipy.optimize import curve_fit
def vorhersage_a1(x, a=1, b=2000):
    return np.exp(a*(x-b))

popt_total = curve_fit(vorhersage_a1, year, total, p0=[1,2000])[0]
popt_fentanyl = curve_fit(vorhersage_a1, year, fentanyl, p0=[1,2000])[0]

timeline = np.arange(1975,2026,1)
total_opt = vorhersage_a1(timeline, *popt_total)
fentanyl_opt = vorhersage_a1(timeline, *popt_fentanyl)

print('\n\n\n#########################################################################################')
print('\t\t\t Aufgabe 1d', '\n')
plt.figure('Aufgabe 1d)')
plt.plot(year, total, 'b-', label=f'Total overdose: data')
plt.plot(year, fentanyl, 'r-', label=f'Fentanyl overdose: data ')
plt.plot(timeline, total_opt, 'b--', label=f'Total overdose: optim with a={popt_total[0]:10.5} and b={popt_total[1]:10.5}')
plt.plot(timeline, fentanyl_opt, 'r--', label=f'Fentanyl overdose: optim with a={popt_fentanyl[0]:10.5} and b={popt_fentanyl[1]:10.5}')
plt.xlabel('Years (1990 to 2020)')
plt.ylabel('Number of Deaths')
plt.legend(loc='best')
plt.grid()
plt.show()


print('\n\n\n#########################################################################################')
print('\t\t\t Aufgabe 1e', '\n')
print(f'Vorhersage der Toten durch Fentanyl: \n\t2023: {vorhersage_a1(2023, *popt_fentanyl)}\n\t2023: {vorhersage_a1(2030, *popt_fentanyl)}')

print('\n\n\n#########################################################################################')
print('\t\t\t Aufgabe 1f', '\n')
ueber = np.floor(timeline[np.min(np.where(fentanyl_opt>total_opt))])
print(f'Vorhersage sagt, dass die Anzahl der Toten durch Fentanyl ab dem Jahr {ueber} die Gesamtüberdosen übersteigen wird')












