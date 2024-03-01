#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                      Vorlesung 11                                     #
#                                                                                       #
#########################################################################################
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
#mplt.use('Qt5Agg')
np.set_printoptions(suppress=True)
#########################################################################################

# ======================================= nächster Teil =================================
print(f'\n\n=====================||  Thema: Fourier Transformation in Python  ||=====================\n')
# =======================================================================================

def dft_homemade(x):
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N,1))
    M = np.exp(-2j * np.pi * k*n/N)
    return np.dot(M,x)

t = np.linspace(0, 6*np.pi, 500)
y = 2*np.sin(2*np.pi*1*t) + 1*np.sin(2*np.pi*1.2*t) + 1

plt.figure()
plt.subplot(221)
plt.plot(t, y)

Y_dft1 = dft_homemade(y)
Y_dft2 = np.fft.fft(y)
plt.subplot(222)
plt.plot(np.abs(Y_dft1), 'g', label='dft_homemade')
plt.plot(np.abs(Y_dft2), 'b', label='Numpy fft')
plt.legend(loc='best')

plt.subplot(223)
plt.plot(np.abs(Y_dft1), 'g', label='dft_homemade')
plt.legend(loc='best')

plt.subplot(224)
plt.plot(np.abs(Y_dft2), 'b', label='Numpy fft')
plt.legend(loc='best')
plt.show()


# --------------------------------------------------------------------------------------
# Normierung und Erstellung des Frequenzvektors
Nf = len(Y_dft2)
f_s = 1/(t[1]-t[0])

Y2_norm = Y_dft2/Nf
Y2_norm_abs = np.abs(Y2_norm)
Y2_norm_abs[1:len(Y2_norm_abs)] *= 2
freqs = np.fft.fftfreq(Nf, d=1/f_s)

plt.figure()
plt.stem(freqs, Y2_norm_abs)
plt.xlabel('Amplitude')
plt.ylabel('Frequenz / Hz')
plt.xlim([0, np.max(freqs)])
plt.show()

print(f"\n\n Übungsaufgabe in VL11 bei 00:49:50, jedoch fehlt die WAV-Datei\nLösung der Übungsaufgabe ab 00:50:50 \n")
# Ich habe ab hier nur noch nachvollzogen, damit ich die Aufgabe nicht anhand meiner Erinnerung lösen kann.
# --------------------------------------------------------------------------------------
'''
wavfile.read gibt als Return ein tupel zurück. 
    - der erste Eintrag (ton[0]) enthält die Abtastrate der Analyse (f_s)
    - der zweite Eintrag (ton[1]) das Array mit zwei Spalten mit den Frequenzdaten. 
      Beide Spalten enthalten dabei die gleichen Informationen


'''
# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print(f"Vorlesung`s Video weiter bei 00:00:00")
