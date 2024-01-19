#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 03
#
#_______________________________________________________________________
import numpy as np
import scipy as sc
from math import *
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
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
#==================================================================================
#x=float(input('x='))
val=0.0
x=0.
i=0
while x<=3.*pi:
    x+=pi/5
    if 0<=x<=pi:
        val =sin(x)
    elif pi< x <= 2*pi:
        val=-sin(x)
    elif 2*pi < x <= 3*pi:
        val=sin(x)
    else: val=0.0
    print(' i= %-4g x=%-8g y=%-8g'%(i,x,val))
    i+=1

#======================================== Teil 02 =================================
print(f'\n\n=====================\n||     Thema 1     ||\n=====================\n')
#==================================================================================





#========================== Ende =======================================
print("\n\n",'============= Vorlesung beendet =============',"\n\n")
#=======================================================================