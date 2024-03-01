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
# plt.tight_layout(pad=0.5)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1.0', '\n')
def data_to_dic(datanamelist):
    folderpath=r'C:\Users\User\OneDrive\Uni und Verbindung\Uni und aktuelles Semester\Aktuelles Semester\WiSe 2324 - Simulation technischer Systeme mit Python\Eigene Programme\Simulation_mit_Python\Ueben_Klausur'
    l=len(datanamelist)

    dic = dict()

    for n in range(l):
        datapath = folderpath+'\\'+datanamelist[n]
        datafile = open(datapath,'r')
        data = []
        for line in datafile:
            data.append(line)
        datafile.close()

        ''' editieren der daten'''
        datatitle = []
        datatime = []
        datavalue = []

        datatitle = str(data[0])
        datatime = data[1].split(' ')
        datatime[0] = datatime[0].replace('\n', '')
        datatime[1] = datatime[1].replace('-',',')
        datatime[1] = datatime[1].replace('\n','')

        datavalue = data[2].split(' ')
        datavalue[0] = datavalue[0].replace('\n', '')
        datavalue[1] = datavalue[1].replace(',', '.')
        datavalue[1] = datavalue[1].replace('-', ',')
        datavalue[1] = datavalue[1].replace('\n','')

        ''' Speichern der Daten'''
        dic[datatitle] = {str(datatime[0]): list(map(float, datatime[1].split(','))),
                          str(datavalue[0]): list(map(float, datavalue[1].split(',')))}
        print(f'Datei {n+1} complett')
        plt.plot(dic[datatitle][str(datatime[0])], dic[datatitle][str(datavalue[0])], label=datatitle)
        plt.xlabel(str(datatime[0]))
        plt.ylabel(str(datavalue[0]))
    print(' ')
    plt.legend()
    plt.grid()
    plt.show()
    return dic

datalist = ['data_export.txt','data_export2.txt']
daten = data_to_dic(datalist)
for key1, value1 in daten.items():
    print(key1.replace('\n', ''))
    for key2, value2 in value1.items():
        print(f" \t", key2, f":\t", value2)
    print('  ')


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2.0', '\n')
plt.figure()
for w in [1,2]:
    t = np.arange(0, 10.001, 0.001)
    y1 = []
    y2 = []

    for z in t:
        p2=0
        p5=0
        for n in range(2):
            k=(1+2*n)
            p2 += 4/(k*np.pi) * np.sin(k*w*z)

        for m in range(5):
            k=(1+2*m)
            p5 += 4/(k*np.pi) * np.sin(k*w*z)
        y1.append(p2)
        y2.append(p5)

    plt.subplot(2,1,w)
    plt.plot(t,y1,label='y1')
    plt.plot(t,y2,label='y2')
    plt.title(f'Taylorentwicklung mit w={w}')
    plt.legend(loc='best')
    plt.grid()
plt.tight_layout(pad=0.5)
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 3.0', '\n')
for i in reversed(range(1,5)):
    plt.figure(1)
    daten = np.random.normal(5,0.1*i,10000)
    n, bins, patches = plt.hist(daten,50)
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 4.0', '\n')
genau = 1
t = np.arange(0, 100, genau)
sinus = []
matrixplot = np.zeros([42,len(t)])
for z in t:
    s=round(mth.sin(z/10), 1)
    sinus.append(s)
    matrixplot[int(20*s+20)][int(z/genau)] = 100
print(t)
print(sinus)
plt.matshow(matrixplot)
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 6.0', '\n')

plt.figure()
t=np.arange(0,2*np.pi+np.pi/30,np.pi/30)
y=np.sin(t)**2

plt.subplot(221)
X='lin'
Y='lin'
plt.plot(t,y,'o-')
plt.title(f'X: {X} | Y: {Y}')
plt.xlabel(f'X-Skalierung: {X}')
plt.ylabel(f'Y-Skalierung: {Y}')
plt.grid()

plt.subplot(222)
X='lin'
Y='log'
plt.semilogy(t,y,'o-')
plt.title(f'X: {X} | Y: {Y}')
plt.xlabel(f'X-Skalierung: {X}')
plt.ylabel(f'Y-Skalierung: {Y}')
plt.grid()

plt.subplot(223)
X='log'
Y='lin'
plt.semilogx(t,y,'o-')
plt.title(f'X: {X} | Y: {Y}')
plt.xlabel(f'X-Skalierung: {X}')
plt.ylabel(f'Y-Skalierung: {Y}')
plt.grid()

plt.subplot(224)
X='log'
Y='log'
plt.loglog(t,y,'o-')
plt.title(f'X: {X} | Y: {Y}')
plt.xlabel(f'X-Skalierung: {X}')
plt.ylabel(f'Y-Skalierung: {Y}')
plt.grid()

plt.tight_layout(pad=0.5)
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 7.0', '\n')











