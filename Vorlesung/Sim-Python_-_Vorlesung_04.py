#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Vorlesung 04
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

f=lambda x:x**2.+4
val=f(2)
print('val= %20.2f' %val)

#======================================== Teil 02 =================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
#==================================================================================
temp=[21.8, 18.1, 19, 23, 26, 17.8]
f=lambda x: sum(x)/len(x)
arith_mittel=f(temp)
print('Das Arithmetrische Mittel der Temperaturen',temp,'[°c] ist %5.2f [°c]' %(arith_mittel))




#========================== Ende =======================================
print("\n\n",'============= Vorlesung beendet =============',"\n\n")
#=======================================================================