#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Übung 04
#
# _______________________________________________________________________
import numpy as np
import scipy as sc
import matplotlib.pyplot  as plt
from matplotlib.ticker import MultipleLocator
import pytest
# -----------------------
import os
import csv
import sys
import serial
from datetime import datetime
import _thread as thread
import time
from copy import copy
from sympy import true
# -----------------------
import Uebung_04_testfunk
import Uebung_04_class
# -----------------------
os.system('clear')
os.system('cls')
print("\n\n\n")
# ======================================== Teil 00 =================================
print(f'\n\n=====================\n||   Aufgabe 1.0   ||\n=====================\n')
# ==================================================================================
class HoleDetection:
    """
        Hole describes a general hole
        """

    name = 'Hole'
    class_counter = 0

    def __init__(self):
        """
                Initialising an instance of the class hole sets the centre point of the hole at the coordinates (0/0)
                """
        Hole.class_counter += 1
        self._centre_point = (0, 0)
    @property
    def (self):
        return 
    
    @.setter
    def (self, value):
        pass
def test_hole_detection():
    pass
# ========================== Ende =======================================
print("\n\n")