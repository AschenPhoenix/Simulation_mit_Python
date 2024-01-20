#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 05
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

from sympy import true
#-----------------------
os.system('clear')
os.system('cls')
print("\n\n\n")
#======================================== Teil 01 =================================
print(f'\n\n=====================\n||     Thema 1     ||\n=====================\n')
#==================================================================================
matrix1 = np.array([[1,2,3,5],[4,5,6,8],[7,8,9,1]])
print(matrix1,'\n')
matrix3 = np.transpose(matrix1)
print(matrix3,'\n')
matrix3 =matrix1.T
print(matrix3,'\n')

#======================================== Teil 02 =================================
print(f'\n\n=====================\n||     Thema 2     ||\n=====================\n')
#==================================================================================
vektor1 = np.array([0,1,2,3])
vektor2 = np.array([2,2,2,2])
print(vektor1,vektor2,'\n ----')

print(vektor1+vektor2,'\n')
print(vektor1*vektor2,'\n ----')

vek_prod = np.outer(vektor1,vektor2)
print(vek_prod,type(vek_prod),'\n')
scallar = np.inner(vektor1,vektor2)
print(scallar,type(scallar),'\n')
scallar = np.dot(vektor1,vektor2)
print(scallar,type(scallar),'\n')

#kreuzprod = np.cross(vektor1,vektor2) # Hat zu viele Elemente! Kann nur bis 3 Stellen
vektor3 = np.array([1,2,3])
vektor4 = np.array([2,2,2])
kreuzprod = np.cross(vektor3,vektor4)
print(kreuzprod,type(kreuzprod),'\n ----')

print(vektor1[3])
print(vektor1[1:3])
print(vek_prod[:,2])
print(vek_prod[1:3,1:3]) # Hierbei wird jeweis die 3 Zeile bzw, Spalte ausgeschlossen

#======================================== Teil 03 =================================
print(f'\n\n=====================\n||     Thema 3     ||\n=====================\n')
#==================================================================================
print(np.logspace(1,5,4,base=2))

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||     Thema 4     ||\n=====================\n')
#==================================================================================
arry_from_func = np.fromfunction(lambda i, j: i==j, (2,3), dtype=int)
print(arry_from_func,type(arry_from_func),'\n')

f=lambda m, n: n+10*m
A=np.fromfunction(f, (6,6), dtype=int)
print(A,type(A),'\n')
print(A[1:3,1:3])

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||     Thema 5     ||\n=====================\n')
#==================================================================================
'''Lineares Gleichungssystem Lösen
__________________________________
1*x1 + 2*x2 = 5
3*x1 + 4*x2 = 11

ges: x=[x1 x2]'''

A=np.array([[1,2],[3,4]])
b=np.array([[5],[11]])
y=np.linalg.solve(A,b)
print(y,'\n')

#======================================== Teil 02 =================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
#==================================================================================
from scipy.interpolate import interp1d

x=np.linspace(0,2*np.pi, 8)
x2=np.linspace(0,2*np.pi, 80)

y=np.sin(x)
y2=np.sin(x2)

f= interp1d(x,y,kind='linear')
print(f,'\n')

fx2 = f(x2)
print(fx2,'\n')

diff =abs(y2-fx2)
max_diff = max(diff)
print('Maximale Differenz: ',max_diff)

plt.plot(x2,y2,"b-",linewidth=3,label='sin(x)')
plt.plot(x2,fx2,"r-",linewidth=3,label='interpolation von sin(x)')
plt.scatter(x,y,s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()




#========================== Ende =======================================
print("\n\n",'============= Vorlesung beendet =============',"\n\n")
#=======================================================================