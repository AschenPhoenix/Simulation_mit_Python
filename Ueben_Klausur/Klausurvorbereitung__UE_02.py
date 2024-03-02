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

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 0.0', '\n')
Alexander = {'Vorwissen': int(7), 'Programmiersprachen': ['C++', 'Matlab', 'Python'], 'Erwartungen':'Bestehen der Klausur' }
print(Alexander)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 1.0', '\n')

string = ''
for j in range(1,10):
    for i in range(1,10):
        string += str(j*i) + '\t'
    string += '\n'
print(string)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2.0', '\n')
string = "56,756,756,7,452,34534,7,65,845,35,345,37,56,3,3,523,1,235,135,57,857,845,745,632,56,58,568,5,1"
print(string)
string=string.replace(',','.')
print(string)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 3.0', '\n')
liste=np.arange(1,42.1,0.1)
print(liste)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 4.0', '\n')
n=50
liste=[]
zeilen=range(len(liste))
for j in range(n):
    liste.append(np.random.randint(1,1000))
for i in zeilen:
    if (liste[i] % 2) !=0:
        del liste[i]
        del zeilen[-1]
print(liste)


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 8.0', '\n')
liste = []
for i in range(100):
    liste.append(random.randint(0,10))
tuple1=tuple(liste)
zahl1 = input('Welche Zahl soll gezählt werden? ')
anzahl = tuple1.count(int(zahl1))

print("Die Zahl %i tritt insgesamt %i mal auf." % (int(zahl1),anzahl))
print(f"Die Zahl {zahl1} tritt insgesamt {anzahl} mal auf.")


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 9.0', '\n')
wiederholen=True
x = 0
while wiederholen:
    x=np.random.randint(1,6)
    print(f'\nDu hast eine  {x}  gewürfelt\n')
    wiederholen=bool(input(f'Willst  du nochmal würfen?  (Antwort: ja, nein)\n\t'))
    if wiederholen != 'ja': break


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 10.0', '\n')
filename = "../src_extern_data/MeineDaten.xlsx"
file = opx.load_workbook(filename)
data = file['Tabelle1']
l = len(data['A'])

Daten = {data['A1'].value: [], data['B1'].value: [], data['C1'].value: []}
for i in range(2,l):
    Daten[data['A1'].value].append(float(data['A' + str(i)].value))
    Daten[data['B1'].value].append(float(data['B' + str(i)].value))
    Daten[data['C1'].value].append(float(data['C' + str(i)].value))
for key, value in Daten.items():
    print(key, f":\t", value)
file.close()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 11.0', '\n')
t = Daten['Zeit']
y= np.sin(t)**2
y=y.tolist()
print(f't = {t}')
print(f'y = {y}')
plt.plot(t,y)
plt.show()

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 13.1', '\n')
def Polynom(x,a=1,b=1,c=00):
    f=a*x**2+b*x+c
    return f

print('\n\n\n', '\t\t\t Aufgabe 13.2', '\n')
x=np.arange(0,10.2,0.2)
y=Polynom(x,2,-10,4)
plt.plot(x,y)
#plt.show()

print('\n\n\n', '\t\t\t Aufgabe 13.3', '\n')


print('\n\n\n', '\t\t\t Aufgabe 13.4', '\n')
def PolyDiff(x,y):
    ydiff=[]
    for i in range(1,len(x)-1):
        ydiff.append((y[i+1]-y[i-1])/(2*(x[i+1]-x[i])))
    return ydiff

print('\n\n\n', '\t\t\t Aufgabe 13.5', '\n')
plt.plot(x[1:-1],PolyDiff(x,y))
plt.show()


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 14.0', '\n')

def someFunc(f1,f2,f3):
    summe = f1+f2+f3
    produkt = f1*f2*f3
    maximal = max([f1,f2,f3])
    minimal = min([f1,f2,f3])
    return summe,produkt,[maximal,minimal]

fsum, fprod, fmaxima = someFunc(5,6,7)
print(f'fsum={fsum}, fprod={fprod}, fmaxima={fmaxima}')

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 15.0', '\n')
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
    print(' ')
    return dic

datalist = ['data_export.txt','data_export2.txt']
daten = data_to_dic(datalist)
for key1, value1 in daten.items():
    print(key1.replace('\n', ''))
    for key2, value2 in value1.items():
        print(f" \t", key2, f":\t", value2)
    print('  ')


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 16.0', '\n')