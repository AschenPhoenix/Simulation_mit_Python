#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 01
#
#_______________________________________________________________________
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
os.system('clear')
os.system('cls')
print("\n\n\n")
#========================= Teil 01 =====================================
#_________________________
# Rechenoperationen
print(5+26)
print(43*5)
print(84/3)
# print(84:3)
print(3*4)
print(3**4)
print(-3**4)
print((-3)**4)
print(4/2)
print(-3.**4)
print((3-5j)**3)
print(4//3)
print(1//2)
print("\n\n")
#_________________________
# Listen
p=[1,3,5,7]
print(2 in p)
print(5 in p)

O=[1,2,'hallo world ',3,6,9]
Q=[22,4,'the Python Team is speaking']
print(O+Q)

print(p[0])
print(O[2])
print(Q[1])

R=O+Q
print(R)
print(R[-1])

# S=R[2:3]+R[-1]
S1=R[-1]
S2=R[2]
S=S2+S1
print(S)

#print(min(R))
T=[1,3,5,7,9]
U=[2,4,6,8,10]
print(min(T))
print(max(U))

V=['x','y','z']
print(min(V))
W=2*V
print(W)
print("\n\n")
#_________________________
# Vordefinierte Variablen
from math import pi
print(pi)
from math import e
print(e)

from math import * # Importiert alles aus Bibliothek "math"
print(cos(pi/2))
print(sin(pi/2))

print(pi)
print(np.pi)
print(np.e)
print(np.tan(pi))

e=3.0
print(e)
print(np.e)
print("\n\n")
#========================== Ende =======================================
print("\n\n",'============= Vorlesung beendet =============',"\n\n")
#=======================================================================