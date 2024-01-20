#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Übung 05
#
#_______________________________________________________________________
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
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
# import cv2
# -----------------------
from Uebung_04_class import HoleDetection
# -----------------------
# os.system('clear')
os.system('cls')
print("\n\n\n")

def test_holedetection():
    hole_detection = HoleDetection(filename='holes.JPG', filepath='../Uebung/')
    variable_type = type(hole_detection)
    print(variable_type)
    pass

test_holedetection()