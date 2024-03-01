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

D=np.arange(0,1.1,0.1)
np.round(D,3)
eta = np.linspace(0,5,501)

V=[]
for di in D:
    V.append(1/(np.sqrt((1 - eta ** 2) ** 2 + (2 * di * eta) ** 2)))

plt.figure()
for i in range(len(D)):
    plt.semilogy(eta,V[i],label=f'V für D={i/10}')
plt.xlabel(r'Frequenzverhältnis $\eta$')
plt.ylabel('Vergrößerungsfunktion V')
plt.title('Vergrößerungsfunktion Einmassenschwinger')
plt.legend(loc='best')
plt.grid()
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 8.0', '\n')

# Leistung
n2=np.array([1000.000, 1384.615, 1707.692, 2015.385, 2338.462, 3015.385, 3523.077, 4015.385, 4461.538, 5015.385, 5615.385, 6015.385])
P2 =np.array([4.538, 11.626 , 17.868, 23.581, 30.141, 40.401, 45.900, 50.551, 53.615 , 54.983 , 53.174 , 50.309])

n1=np.linspace(1000,6100,100)
T =np.array([-1.3500e-13, 2.9643e-09, -2.5004e-05, 0.0779, 59.9732])
P1 =np.polyval(T,n1)


fig, ax1 = plt.subplots()

# linke Y-Achse
pl1 = ax1.plot(n1,P1,'b', label='Drehmoment T')
ax1.set_ylim([0, 161])
ax1.set_ylabel('Drehmoment', color='b')

ax1.set_xlim([900, 6100])
ax1.set_xlabel('Drehzahl', color='k')

# rechte Y-Achse
ax2 = ax1.twinx()
pl2 = ax2.plot(n2,P2,'go-',label='Leistung P')
ax2.set_ylim([0, 61])
ax2.set_ylabel('Leistung', color='g')

plt.title('Motorkennlinie Golf 3 AAM')
plt.legend(loc='best')
ax1.grid(color='b')
ax2.grid(color='g')
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 9.3', '\n')
a = 5
b = np.array([[15,30,1]]) # doppelte [] um ein 2D array zu erstellen
b2 = np.array([15,30,1]) # beachte Dimensionsunterschied zu b
C = np.array([[1,2,0],[5,3,82],[47,6,3]])
E = np.array([[1,2,3],[5,4.5,4],[0,100,200]])
F = np.array([[1,0,87,46],[9,2,8,3],[25,7,11,6],[23,15,1,3]])
print(np.dot(b,b.T))
print(b@b.T) # @ kann statt np.dot genutzt werden
print(b.T@b)
print(np.outer(b2,b2)) # so geht es mit einem 1D array
print(np.linalg.det(C))
print(np.linalg.inv(F))
print(F@np.linalg.inv(F)) # beachtet die numerischen Fehler
print(C+E)
print(C-E)
print(C*E)
print(np.dot(np.diagonal(C),b[0,:]))
print(np.dot(np.diagonal(C),b2))
print(C[:,2]+b)