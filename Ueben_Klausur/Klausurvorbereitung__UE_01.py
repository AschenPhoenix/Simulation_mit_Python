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
print('\n\n\n', '\t\t\t Aufgabe 2.2', '\n')
# 2.2
pi=3.141592653589793238462643383279502884197169399375105
print(f'pi={pi:7.6}')

print('\n\n\n', '\t\t\t Aufgabe 2.4', '\n')
print(f'\"Python\" ist eine tolle Programmiersprache')

print('\n\n\n', '\t\t\t Aufgabe 2.5', '\n')
String = f'\"Python\" ist eine tolle Programmiersprache'
String = String.replace('\"Python\" ist', '\"C++\" ist auch')
print(String)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 3.1', '\n')
MyText = ("Python ist eine universelle, üblicherweise interpretierte höhere Programmiersprache. Sie hat den Anspruch, einen gut lesbaren, knappen Programmierstil zu fördern. So werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch Einrückungen strukturiert. Wegen seiner klaren und übersichtlichen Syntax gilt Python als einfach zu erlernen. Python unterstützt mehrere Programmierparadigmen, z.B. die objektorientierte, die aspektorientierte und die funktionale Programmierung. Ferner bietet es eine dynamische Typisierung. Wie viele dynamische Sprachen wird Python oft als Skriptsprache genutzt. Die Sprache weist ein offenes, gemeinschaftsbasiertes Entwicklungsmodell auf, das durch die gemeinnützige Python Software Foundation gestützt wird, die de facto die Definition der Sprache in der Referenzumsetzung CPython pflegt.")

def textsuche(Text=MyText):
    # stichwort = input('Bitte stichwort eingeben, nach dem gesucht werden soll:\n')
    stichwort = 'die'
    stelle = MyText.find(stichwort)
    anzahl = MyText.count(stichwort)

    if (stelle+1)<0:
        print(f'\n\tDieses Stichwort ist nicht im Text enthalten!\n')
    else:
        print(f'\n\tDas Stichwort \"{stichwort}\" ist {anzahl}-mal im Text enthalten. \n\t\tDer erste Fundort ist ab dem {stelle+1}-Zeichen!\n')
pass

textsuche()

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 4.1', '\n')
print(np.linspace(0,10,11))

print('\n\n\n', '\t\t\t Aufgabe 4.4', '\n')
x=[2, 4, 1, 7, 6, 10, 9, 5, 3, 8]
y = x.copy()
y.sort()
print(f'Unsortiert:\t {x} \n Sortiert:\t {y}')

print('\n\n\n', '\t\t\t Aufgabe 4.3', '\n')
def textsuche2(Text=MyText):
    # stichwort = input('Bitte stichwort eingeben, nach dem gesucht werden soll:\n')
    stichwort = 'die'
    anzahl = MyText.count(stichwort)
    stellen = []
    i=0
    j=0
    for i in range(anzahl):
        x=MyText.find(stichwort, j)
        stellen.append(x+1)
        j=x+1

    if anzahl == 0:
        print(f'\n\tDieses Stichwort ist nicht im Text enthalten!\n')
    else:
        print(f'\n\tDas Stichwort \"{stichwort}\" ist {anzahl}-mal im Text enthalten und an den Stellen {stellen} zu finden\n')
pass
textsuche2()


print('\n\n\n', '\t\t\t Aufgabe 4.5', '\n')