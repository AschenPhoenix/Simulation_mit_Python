#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                      Vorlesung 08                                     #
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
# np.set_printoptions(suppress=True)
#########################################################################################

# ======================================= nächster Teil =================================
print(f'\n\n=====================\n||  Thema 3.0  ||\n=====================\n')
# =======================================================================================
print(f'===> Thema: Lineares Gleichungssystem <===')
'''
- Um ein lineares Gleichungssystem zu lösen, müssen wir die Inverse der Matrix bilden (A * x = b => x = A^-1 * b)
- Die Determinante der Matrix muss größer sein als Null.
  [d=np.linalg.det(A)]
- Um die Inverse bilden zu können, muss die Matrix A NICHTSINGULÄR (A * A^-1 = A^-1 * A = I) sein, weil sonst keine
  Inverse zu dieser Matrix gebildet werden kann. 
  [I=np.dot(A, np.linalg.inv(A))]
- Zudem darf die Matrix nicht SCHLECHT KONDITIONIERT sein. 
  Ein Maß für die Konditionierung einer Matrix ist:
  [c=np.linalg.cond(A)]
'''

class LGS_System:
    def __init__(self, A, b):
        np.set_printoptions(suppress=True)
        self._A = []
        self._b = []
        self._detA = 0
        self._invA = []
        self._condA = 0
        self._lsg = []

        self._A = A
        self._b = b
        self.detA()
        self.condA()
        self.invA()
        self.LGS_loesen()

    @property
    def A(self):
        return self._A

    @property
    def b(self):
        return self._b

    def detA(self):
        self._detA = np.linalg.det(self._A)
        print(f'Determinante: det(a)={self._detA:.3f}')
        return self._detA

    def condA(self):
        self._condA = np.linalg.cond(self._A)
        print(f'Konditionszahl: cond(A) = {self._condA:.3f}')
        return self._condA

    def invA(self):
        try:
            self._invA = np.linalg.inv(self._A)
            print(f'Singularitätstest: A * A^-1 :\n {np.dot(self._A, np.linalg.inv(self._A))}')
        except:
            self._invA = None
            print(f'Matrix ist nicht Invertierbar, da sie nicht Singulär ist!')
        return self._invA

    def LGS_Info(self, verbose=0):
        self._detA = np.linalg.det(self._A)
        self._condA = np.linalg.cond(self._A)
        try:
            self._invA = np.linalg.inv(self._A)
        except:
            self._invA = None

        if verbose:
            print(f'\n\n================================ Eq. System Info ================================ ')
            print(f'System Matrix: A \n {self._A}')
            print(f'\nLösungsvektor: b \n {self._b}')
            print(f'\nDeterminante: \ndet(a)={self._detA:.3f}')
            print(f'\nKonditionszahl: \ncond(A) = {self._condA:.3f}')
            print(f'\nSingularitätstest: A * A^-1')
            if self._invA is not(None):
                print(f'{np.dot(self._A, np.linalg.inv(self._A))}')
            else:
                print(f'Matrix ist nicht Invertierbar, da sie nicht Singulär ist!')
            print(f'\nLösung des LGS ist x = {self._lsg}')
            print(f'================================================================================= ')
        return ([self._detA, self._condA, self._invA])

    def LGS_loesen(self):
        print('\n')
        try:
            self._lsg = np.linalg.solve(self._A, self._b)
            print(f'Matrix ist invertierbar, daher Lösung mit Solver:')
            print(f' ===> Lösung für x = {self._lsg}')
        except:
            print(f'Matrix ist "NICHT" invertierbar!')
            print(f'Lösung mit Pseudo-Inverse \n{np.linalg.pinv(self._A)} \nmöglich, besser aber über Annäherung')
            self._lsg = np.linalg.lstsq(self._A, self._b, rcond=-1)[0]
            print(f'\n===> Näherungslösung für x = {self._lsg}')
        return self._lsg

    # -----------------------------------------------------------------------------------------------------------
    @property
    def matrix(self, A, b):
        self._A = A
        self._b = b
        pass

    @matrix.setter
    def matrix(self, value1, value2):
        self._A = value1
        self._b = value2
        self.detA()
        self.condA()
        self.invA()

'''
# -----------------------------------------------------------------------------------
print(f'------- System 1 -------')
A1 = np.array([[1, -2, 1], [2, 1, -1], [-1, -4, 3]])
b1 = np.array([6, -3, 14])

det_1 = np.linalg.det(A1)
inv_1 = np.linalg.inv(A1)
print(f'Determinante: det(a)={det_1:.3f}')                # :.3f dient zur anpassung der Nachkommastellen in f-Strings
print(f'Singularitätstest: A * A^-1 :\n {np.dot(A1, np.linalg.inv(A1))}')
print(f'Konditionszahl: cond(A) = {np.linalg.cond(A1):.3f}')

# -------------------------------
print(f'\n\n------- System 2 -------')
A2 = np.array([[1, 2, 2], [2, 3, 1], [3, 5, 3]])
b2 = np.array([-2, 1, -1])

det_2 = np.linalg.det(A2)
inv_2 = np.linalg.inv(A2)
print(f'Determinante: det(a)={det_2:.3f}')                # :.3f dient zur anpassung der Nachkommastellen in f-Strings
print(f'Singularitätstest: A * A^-1 :\n {np.dot(A2, np.linalg.inv(A2))}')
print(f'Konditionszahl: cond(A) = {np.linalg.cond(A2):.3f}')
# -------------------------------
print(f'\n\n------- System 3 -------')
A3 = np.array([[1, 1, 1], [3, 3, 3], [5, 5, 5]])
b3 = np.array([3, 4, 9])

det_3 = np.linalg.det(A3)

print(f'Determinante: det(a)={det_3:.3f}')                # :.3f dient zur anpassung der Nachkommastellen in f-Strings
print(f'Konditionszahl: cond(A) = {np.linalg.cond(A3):.3f}')
try:
    inv_3 = np.linalg.inv(A3)
    print(f'Singularitätstest: A * A^-1 \n {np.dot(A3, np.linalg.inv(A3))}')
except:
    print(f'Matrix ist nicht Invertierbar, da sie nicht Singulär ist!')
'''
print('-----------------------------------------------------------------------------------------------------------')
print(f'\n\n------------------------ System 1 ------------------------')
A1 = np.array([[1, -1, 1], [2, 1, -1], [-1, -4, 3]])
b1 = np.array([6, -3, 14])
system_1 = LGS_System(A = A1,  b = b1)
system_1.LGS_Info(verbose=1)
# system_1.matrix(A=A1, b=b1)

print('-----------------------------------------------------------------------------------------------------------')
print(f'\n\n------------------------ System 2 ------------------------')
A2 = np.array([[1, 2, 2], [2, 3, 1], [3, 5, 3]])
b2 = np.array([-2, 1, -1])
system_2 = LGS_System(A = A2,  b = b2)
system_2.LGS_Info(verbose=1)

print('-----------------------------------------------------------------------------------------------------------')
print(f'\n\n------------------------ System 3 ------------------------')
A3 = np.array([[1, 1, 1], [3, 3, 3], [5, 5, 5]])
b3 = np.array([3, 4, 9])
system_3 = LGS_System(A = A3,  b = b3)
system_3.LGS_Info(verbose=1)

# ====================================== nächster Teil ==================================
print(f'\n\n=======================\n||   Bsp Aufgabe 1   ||\n=======================\n')
# =======================================================================================

# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Vorlesung's Video weiter bei 00:00:00')
