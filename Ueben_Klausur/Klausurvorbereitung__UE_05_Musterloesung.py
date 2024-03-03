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
print('\n\n\n', '\t\t\t Aufgabe 2.0', '\n')

### Aufgabe 3 ####################################
def conv(x):
    return x.replace(',', '.')

filePath = '../src_extern_data/'

results = {} # Dictionary erstellen
Emoduln = []
VLast = []

def calcEModul(strain,stress):
    # search for position of 0,05% and 0,25% in strain data
    pos05 = np.nanargmin(np.abs(strain-0.0005)) # nanargmin kann mit nan umgehen!
    pos25 = np.nanargmin(np.abs(strain-0.0025))
    p = np.polyfit(strain[pos05:pos25],stress[pos05:pos25],1)
    return p

# Load results into a dict
for i in range(5):
    fileName = '\Specimen_RawData_' + str(i+1) + '.csv'
    rawData = np.genfromtxt((conv(x) for x in open(filePath+fileName)),delimiter=";",skip_header=6)
    results[str(i+1)] = {'movement': rawData[:,1]/1000,
                         'force': rawData[:,2]*1000,
                         #'strain': rawData[:,1]/1000/0.15,
                         'strain': rawData[:,3]/100,
                         'stress': rawData[:,2]*1000/(3.4*1e-6)} # Dict im Dict erstellen
    # negative werte sind physikalisch nicht sinnvoll und entstehen durch
    # das Abnehmen des Sensors im Versuch. Daher bereinige ich das zu nan
    results[str(i+1)]['strain'][results[str(i+1)]['strain'] < 0] = np.nan

    results[str(i+1)]['fitParam'] = calcEModul(results[str(i+1)]['strain'],results[str(i+1)]['stress'])
    results[str(i+1)]['EModul'] = calcEModul(results[str(i+1)]['strain'],results[str(i+1)]['stress'])[0]
    results[str(i+1)]['Versagenslast'] = np.max(results[str(i+1)]['force'])
    Emoduln.append(results[str(i+1)]['EModul'])
    VLast.append(results[str(i+1)]['Versagenslast'])

    plt.figure(1)
    plt.plot(results[str(i+1)]['movement']*1000,results[str(i+1)]['force'])
    plt.xlabel('Traversenweg / mm')
    plt.ylabel('Kraft / N')

    plt.figure(2)
    plt.plot(results[str(i+1)]['strain']*100,results[str(i+1)]['stress']/1e9)

plt.plot(results[str(i+1)]['strain']*100,(results[str(i+1)]['EModul']*results[str(i+1)]['strain']+results[str(i+1)]['fitParam'][1])/1e9)
plt.xlabel('Dehnung / %')
plt.ylabel('Spannung / GPa')

plt.figure(3)
plt.subplot(121)
plt.hist(np.array(Emoduln)/1e9)
plt.title('EModuln / GPa')
plt.subplot(122)
plt.hist(np.array(VLast))
plt.title('Versagenslast / N')
plt.show()

