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
x = np.linspace(0, 2*np.pi, 500)
y_1 = np.sin(x**2)

#-------------------------------
''' Wichtige Sache zu wissen!'''
plt.plot(x, y_1, label=r'$sin(x^2)$ + $\int_{x=0}^{x=10}3x$') # r zeigt an das die Schreibweise von LaTex verwendet werden soll, wodurch x^2 in Mathematischer Schreibweise dargestelt wird
#-------------------------------

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

#======================================== Teil 01 =================================

x = np.linspace(0, 2*np.pi, 500)
y_1 = np.sin(x**2)
y_2 = np.sin(x**2)*0.6

#-------------------------------
plt.plot(x, y_1, 'k', linewidth=0.5, label=r'$sin(x^2)$')
plt.plot(x, y_1*0.2, 'k-.', linewidth=0.5, label=r'$sin(x^2)*0.2$')
plt.plot(x, y_1*0.3, 'k->', linewidth=0.5, label=r'$sin(x^2)*0.3$')
plt.plot(x, y_1*0.4, 'k-x', linewidth=0.5, label=r'$sin(x^2)*0.4$')
plt.plot(x, y_1*0.5, 'k-3', linewidth=0.5, label=r'$sin(x^2)*0.5$')
plt.plot(x, y_2, 'k-+', linewidth=1, markevery=20, label=r'$sin(x^2)*0.6$') #So wird nicht jeder Datenpunkt markiert und es wird übersichtlicher
#-------------------------------

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

#======================================== Teil 01 =================================

x = np.linspace(0, 2*np.pi, 500)
y_1 = np.sin(x**2)
y_2 = np.sin(x**2)*0.6

#-------------------------------
markerListe=['.','o','>','d','3']

for mar in markerListe:
 plt.plot(x, y_2, marker=mar, linewidth=1, markevery=10, label=r'$sin(x^2)*0.6$')

plt.grid()
plt.legend()
plt.show()
#-------------------------------
for i, mar in enumerate(markerListe):
 plt.plot(x, y_1-i, marker=mar, linewidth=1, markevery=10, label=r'$sin(x^2)$ - {}'.format(i))

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()




#======================================== Teil 02 =================================
print(f'\n\n=====================\n||     Thema 2     ||\n=====================\n')
#==================================================================================
plt.figure()
x = np.linspace(0, 2*np.pi, 500)
y = np.exp(x)
plt.subplot(4,2,1)
plt.plot(x,y,label=r'$e^{x}$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()


plt.subplot(4,2,2)
plt.plot(x,y+200,label=r'$e^{x}+200$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()


plt.subplot(4,2,4)
plt.plot(x,y*4,label=r'$e^{x}*4$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.subplot(4,2,5)
plt.semilogx(x,y,label=r'$e^{x}$ mit log x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.subplot(4,2,6)
plt.semilogy(x,y,label=r'$e^{x}$ mit log y')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.subplot(4,2,7)
plt.loglog(x,y,label=r'$e^{x}$ mit log x,y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('loglog')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=2, wspace=0.5)
plt.show()





#======================================== Teil 02 =================================
print(f'\n\n=====================\n||     Thema 3     ||\n=====================\n')
#==================================================================================
x = np.linspace(0, 2*np.pi, 500)
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
y4=np.tanh(x)

fig=plt.figure("Meine Subplots")
gs=fig.add_gridspec(3,3)

# Achse 1 ----------------
ax1=fig.add_subplot(gs[0,0])
ax1.plot(x,y1)
# Achse 2 ----------------
ax2=fig.add_subplot(gs[0,1])
ax2.plot(x,y2)
# Achse 3 ----------------
ax3=fig.add_subplot(gs[1,0])
ax3.plot(x,y3)
# Achse 4 ----------------
ax4=fig.add_subplot(gs[1,1])
ax4.plot(x,y4)
# Achse 5 ----------------
ax5=fig.add_subplot(gs[2,1:])
ax5.plot(x,y1*200,label=r'$sin(x)$*200')
ax5.plot(x,y2*200,label=r'$cos(x)$*200')
ax5.plot(x,y3,label=r'$tan(x)$')
ax5.plot(x,y4*200,label=r'$tanh(x)$*200')
ax5.set_ylim([-400,600])
ax5.grid()
ax5.legend()


plt.subplots_adjust(hspace=1.5, wspace=0.5)
plt.show()





#======================================== Teil 02 =================================
print(f'\n\n=====================\n||     Thema 4     ||\n=====================\n')
#==================================================================================
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#N=1000
N=50
x=np.linspace(-np.pi,np.pi,N)
y=np.linspace(-np.pi,np.pi,N)

# Raster erstellung
X,Y = np.meshgrid(x,y)
print(f'x ist vom Typ {type(X)}')
print(f'x hat die Größe {x.shape}')
print(X,'\n---------------\n',Y)

# Funktion
Z=np.exp(-(X**2+Y**2))

# Fenster erstellen
fig=plt.figure('3D Plotten')
Zeilen=3
Spalten=3
plt.tight_layout(pad=1)

ax =fig.add_subplot(3,3,3, projection='3d')
ax.plot_surface(X,Y,Z, cmap=cm.jet, label='3D Gauss')
surf=ax.set_title(f'3D Plot mit Colormap "Jet"')
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax =fig.add_subplot(3,3,6, projection='3d')
ax.plot_surface(X,Y,Z, cmap=cm.binary)
ax.set_title(f'3D Plot mit Colormap "Binary"')

ax =fig.add_subplot(3,3,9, projection='3d')
ax.plot_wireframe(X,Y,Z)
ax.set_title(f'3D Netzplot')

ax =fig.add_subplot(3,3,1, projection='3d')
ax.contour(X,Y,Z, cmap=cm.jet)
ax.set_title(f'3D Höhenlinien')

ax =fig.add_subplot(3,3,2, projection='3d')
ax.contourf(X,Y,Z, cmap=cm.jet)
ax.set_title(f'3D Höhenlinien als Oberflächen')

ax =fig.add_subplot(2,2,3)      # Um das besser hin zu bekommen, muss man "gridspec" verwenden
ax.contour(X,Y,Z, cmap=cm.jet)
ax.set_title(f'2D Höhenlinien')

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()

#======================================== Teil 02 =================================
#print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
#==================================================================================


#========================== Ende =======================================
print("\n\n",'============= Vorlesung beendet =============',"\n\n")
#=======================================================================