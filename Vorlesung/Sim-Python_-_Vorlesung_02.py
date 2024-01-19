#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 002
#
#_______________________________________________________________________
from math import sqrt
import math
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib.ticker import MultipleLocator
#-----------------------
import os
import csv
import sys
import serial
from datetime import datetime
import _thread as thread
import time
#-----------------------
print("\n\n\n")
#======================================== Teil 01 =================================
os.system('cls||clear')
print(f'\n\n=====================\n||     Thema 1     ||\n=====================\n')
#==================================================================================

v0=5
t=0.6
g=9.81

y=-0.5*g*t**2+v0*t;
#print("y=-0.5*g*t**2+v0*t hat für v_0=5 t=0.6 g=9.81 den Wert:",y)
print("y=-0.5*g*t**2+v0*t hat für v_0=%2.0f t=%2.1f g=%2.2f den Wert:%1.4fm"%(v0,t,g,y))    # Mit den beginnenden Prozentzeichen und dem abschließenden f, 
print("y=-0.5*g*t**2+v0*t hat für v_0=%2.1f t=%2.1f g=%5.2f den Wert:%7.4fm"%(v0,t,g,y))    # versteht Phyton den Befehl als Formatausgabe:
                                                                                            # - die erste Zahl ist die anzahl der insgesamt freizuhaltenen Zeichenplätze (mit punkt eingerechnet)
                                                                                            # - die zweite Zahl ist die anzahl der Gewünschten Nachkommastellen
                                                                                            # - Ungenutzte Zeichenstellen werden mit Lehrstellen oder Nullen als Nachkommastellen gefüllt


#======================================== Teil 02 =================================
os.system('clear')
#os.system('cls')
print(f'\n\n=====================\n||     Thema 2     ||\n=====================\n')
#==================================================================================
tC=float(input('T=[oC]='))
tF=9/5*tC+32;
print(f'T[oF]=',tF)
#======================================== Teil 02 =================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
#==================================================================================
v0=5
g=9.81
y0=float(input(f'Bitte Hoehe eingeben, welche Hoehe gesucht wird.\nZielhoehe:'))
t0=1/g
t1=(sqrt(-2*g*y0+v0**2))
t2=[t0*(t1+v0),t0*(-t1+v0)]
print('\nZum Zeitpunkt t=%4.3f*(+/-%4.3f+%2.1f)=%5.3f[s] bzw. %5.3f[s] hat der Tennisball die Hoehe yc=%2.0f[m] erreicht!'%(t0,t1,v0,t2[0],t2[1],y))
#======================================== Teil 03 =================================
print(f'\n\n=====================\n||     Thema 3     ||\n=====================\n')
#==================================================================================

print(f'\n\n->    Zip-Funktion in Verbindung mit for-Schleifen nochmal anschauen, könnte wichtig sein!\n\n')
print(f'->    Genauso den Umgang mit Tupeln (a=(1,2,3,...)) und Listen (a=[1,2,3,...]) anschauen!\n      Wird auf jeden fall wichtig werden!\n\n')
#
#
#
#
#========================== Ende =======================================
print("\n\n",'============= Vorlesung beendet =============',"\n\n")
#=======================================================================