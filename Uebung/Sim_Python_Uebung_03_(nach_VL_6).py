"""
Module description
@date: Mai 2020
@author: Hendrik Traub <h.traub@tu-bs.de>
@Copyright: 2020 TU Braunschweig
<www.tu-braunschweig.de>. All rights reserved.
"""
#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Übung 04
#
#_______________________________________________________________________
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib.ticker import MultipleLocator
import serial
from sympy import true
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
#-----------------------
import os
import csv
import sys
from datetime import datetime
import _thread as thread
import time
#-----------------------
os.system('cls')
print("\n\n\n")
#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 2.0   ||\n=====================\n')
#==================================================================================
x=[0]
i=0
while i <= 10:
    i+=0.001
    x.append(i)
w=[1,2,3,4,5]

y1=[]
y2=[]
for v in w:
    f1=[]
    f2=[]
    for t in x:
        f1.append((4/np.pi)*np.sin(v*t) + (4/(3*np.pi))*np.sin(3*v*t))
        f2.append((4/np.pi)*np.sin(v*t) + (4/(3*np.pi))*np.sin(3*v*t) + (4/(5*np.pi))*np.sin(5*v*t) + (4/(7*np.pi))*np.sin(7*v*t) + (4/(9*np.pi))*np.sin(9*v*t))
    y1.append(f1)
    y2.append(f2)
#print(y1,'\n\n',y2)

fig=plt.figure("Uebung 3 - Aufgabe 2")
gs=fig.add_gridspec(3,2)

ax1=fig.add_subplot(gs[0,:])
ax1.plot(x,y1[:][0], 'r', linewidth=1.5, label=r'$y_{1}$(t) = $4/\pi$*sin($\omega$t)+$4/3\pi$*sin(3*$\omega$t)')
ax1.plot(x,y2[:][0], 'g', linewidth=1.5, label=r'$y_{2}$(t) = $4/\pi$*sin($\omega$t)+$4/3\pi$*sin(3*$\omega$t)+$4/5\pi$*sin(5*$\omega$t)+$4/7\pi$*sin(7*$\omega$t)+$4/9\pi$*sin(9*$\omega$t)')
ax1.set_title(f'Polynom der Taylorentwicklung')
ax1.set_xlabel('Zeit t in [s]')
ax1.set_ylabel('Amplitude y')
ax1.grid()
ax1.legend()

ax2=fig.add_subplot(gs[1,:])
ax2.plot(x,y1[:][0], linewidth=1.5, label=r'$y_{1}$(t) mit $\omega$=1')
ax2.plot(x,y1[:][1], linewidth=1.5, label=r'$y_{1}$(t) mit $\omega$=2')
ax2.plot(x,y1[:][2], linewidth=1.5, label=r'$y_{1}$(t) mit $\omega$=3')
ax2.plot(x,y1[:][3], linewidth=1.5, label=r'$y_{1}$(t) mit $\omega$=4')
ax2.plot(x,y1[:][4], linewidth=1.5, label=r'$y_{1}$(t) mit $\omega$=5')
ax2.set_title(r'$y_{1}$(t) mit verschiedenen $\omega$')
ax2.set_xlabel('Zeit t in [s]')
ax2.set_ylabel('Amplitude y')
ax2.grid()
ax2.legend()

ax3=fig.add_subplot(gs[2,:])
ax3.plot(x,y2[:][0], linewidth=1.5, label=r'$y_{2}$(t) mit $\omega$=1')
ax3.plot(x,y2[:][1], linewidth=1.5, label=r'$y_{2}$(t) mit $\omega$=2')
ax3.plot(x,y2[:][2], linewidth=1.5, label=r'$y_{2}$(t) mit $\omega$=3')
ax3.plot(x,y2[:][3], linewidth=1.5, label=r'$y_{2}$(t) mit $\omega$=4')
ax3.plot(x,y2[:][4], linewidth=1.5, label=r'$y_{2}$(t) mit $\omega$=5')
ax3.set_title(r'$y_{2}$(t) mit verschiedenen $\omega$')
ax3.set_xlabel('Zeit t in [s]')
ax3.set_ylabel('Amplitude y')
ax3.grid()
ax3.legend()

plt.subplots_adjust(hspace=0.8)
plt.show()

#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 3.0   ||\n=====================\n')
#==================================================================================
for i in reversed(range(1,5)): 
    plt.figure(1) 
    daten = np.random.normal(5,0.1*i,10000) 
    n, bins, patches = plt.hist(daten,50) 
plt.show()

#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 4.0   ||\n=====================\n')
#==================================================================================
x = np.arange(1,100,1) 
num_y = 20 
y = np.sin(x/5)*num_y+num_y 
A = np.zeros([len(x),2*num_y]) 
for i in range(len(x)): 
    position = int(y[i]) 
    A[i,position] = 1
plt.matshow(A.transpose()) 
plt.show()

#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 5.0   ||\n=====================\n')
#==================================================================================
def matrix_plotten(array,zeile):
    daten=array[zeile][:]
    fig=plt.figure('Uebung 3 - Aufgabe 5')
    plt.plot(range(len(daten)),daten,'c', linewidth=1.5, label=r'Matrix-Zeile {}'.format(zeile))
    plt.title(r'Darstellung der Zeile {} der Matrix'.format(zeile))
    plt.grid()
    plt.xlabel('Spalten der Zeile')
    plt.ylabel('Werte der Spalten')
    plt.legend()
    print('\n Matrix:\n',array)
    print('\n',r'Zeile {} der Matrix:'.format(zeile),'\n',daten)
    plt.show()

n=np.random.randint(2, 10)
m=np.random.randint(2, 10)
k=np.random.randint(0, n-1)
matrix=np.random.rand(n,m)
matrix_plotten(matrix,k)

#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 6.0   ||\n=====================\n')
#==================================================================================
def aufgabe_6_plotten(x):
    y=np.sin(x)**2

    ax1=plt.subplot(411)
    ax1.plot(x,y,'g', linewidth=2, label=r'$y=sin(x)^2$')
    ax1.set_title(f'Plot: X=Linear, Y=Linear')
    ax1.grid()
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.legend()

    ax2=plt.subplot(412)
    ax2.semilogy(x,y,'g', linewidth=2, label=r'$y=sin(x)^2$')
    ax2.set_title(f'Plot: X=Linear, Y=Log')
    ax2.grid()
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.legend()

    ax3=plt.subplot(413)
    ax3.semilogx(x,y,'g', linewidth=2, label=r'$y=sin(x)^2$')
    ax3.set_title(f'Plot: X=Log, Y=Linear')
    ax3.grid()
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.legend()

    ax4=plt.subplot(414)
    ax4.loglog(x,y,'g', linewidth=2, label=r'$y=sin(x)^2$')
    ax4.set_title(f'Plot: X=Log, Y=Log')
    ax4.grid()
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.legend()

    plt.subplots_adjust(hspace=1.2)
    plt.show()
x=np.linspace(-2*np.pi,2*np.pi,50)
aufgabe_6_plotten(x)

#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 7.0   ||\n=====================\n')
#==================================================================================
D=np.linspace(0,1,10);
eta=np.linspace(0,5,100);
for j in range(0,len(D)):
    D[j]=round(D[j],3)

fig=plt.figure('Uebung 3 - Aufgabe 7')
k=1
for i in D:
    V = 1/ (np.sqrt((1-eta**2)**2 + (2*i*eta)**2))
    plt.plot(eta,V, linewidth=1.5, label=r'V mit D={}'.format(i))
    k+=1
plt.xlabel(r'Frequenzverhaeltnis $\eta$')
plt.ylabel(r'Vergroe$\ss$erungsfunktion V')
plt.title(r'Verlauf der Vergroe$\ss$erungsfunktion V für verschiedene Werte des Dämpfungsmaßes D')
plt.grid()
plt.legend()
plt.show()

#======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 8.0   ||\n=====================\n')
#==================================================================================
def drehmoment(n):
    T=[]
    for i in n:
        T0= -(1.3500*np.exp(-13))*i**4 + (2.9643*np.exp(-9))*i**3 - (2.5004*np.exp(-5))*i**2 + 0.0779*i + 59.9732
        T.append(T0)
    return T
n=[1000, 1384.615, 1707.692, 2015.385, 2338.462, 3015.385, 3523.077, 4015.385, 4461.538, 5015.385, 5615.385, 6015.385]
W=[4.538, 11.626, 17.868, 23.581, 30.141, 40.401, 45.9, 50.551, 53.615, 54.983, 53.174, 50.309]

fig, ax1 = plt.subplots()
color=['g','r']
ax1.plot(n,drehmoment(n),color=color[0],linewidth=1.5, label=r'T(n)')
ax1.set_xlabel(r'Drehzahl n in [$1/min$]')
ax1.set_ylabel(r'Drehmoment T')
ax1.set_title(f'Motorkennlinie Golf 3 AAM')
ax1.grid()
ax1.tick_params(axis='y', labelcolor=color[0])

ax2 = ax1.twinx()
ax2.plot(n,W, color=color[1],linewidth=1.5, label=r'W(n)')
ax2.set_ylabel(r'Leistung W in[kW]')
ax2.grid()
ax2.tick_params(axis='y', labelcolor=color[1])

# ask matplotlib for the plotted objects and their labels
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()






#======================================== Teil 00 =================================
print(f'\n\n======================\n||   Aufgabe Numpy   ||\n======================\n')
#==================================================================================
print('======== a) ========\n')
m=5
x1=np.ones(m)
x2=np.ones(m-1)
X=np.diag(2*x1)+np.diag(-1*x2,1)+np.diag(-1*x2,-1)
print(X)



print('\n\n======== b) ========\n')
Y=np.random.rand(6,6)*10
for m in range(0,6):
    for n in range(0,6):
        if n!=m:
            Y[n][m] = Y[m][n]
print(Y)



print('\n\n======== c) ========\n')
a = 5
b = np.array([[15,30,1]]) # doppelte [] um ein 2D array zu erstellen
b2 = np.array([15,30,1]) # beachte Dimensionsunterschied zu b
C = np.array([[1,2,0],[5,3,82],[47,6,3]])
E = np.array([[1,2,3],[5,4.5,4],[0,100,200]])
F = np.array([[1,0,87,46],[9,2,8,3],[25,7,11,6],[23,15,1,3]])

print(np.dot(b,b.T))
print(np.dot(b.T,b),'\n')

print(np.linalg.det(C),'\n')

print(np.linalg.inv(F),'\n')

print(C+E)
print(C-E)
print(C*E,'\n')

print(np.dot(np.diagonal(C),b[0,:]))
print(np.dot(np.diagonal(C),b2),'\n')

print(C[:,2]+b)



print('\n\n======== d) ========\n')





#========================== Ende =======================================
print("\n\n")
#=======================================================================