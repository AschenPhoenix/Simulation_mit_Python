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
import cv2

# |~~~~~~~~~~| Terminal vorbereiten |~~~~~~~~~~|
os.system('cls')
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#                   endregion

# |=======| Import aus anderer Dateien |=======|
#                    region
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
from class_hole import Hole
from class_hole import Circle
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#                   endregion

# |=======| Darstellungseinstellungen |========|
mplt.use('Qt5Agg')
np.set_printoptions(suppress=True)
# plt.tight_layout(pad=0.5)

#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe a', '\n')

'''
def test_hole_detection_a():
    """
    Tests for detection of holes
    Vorlesungsvideo 9 - Zeit: 01:38:00
    :return: None
    """
    hole_detection = HoleDetection(filename='holes.JPG', filepath='../src_extern_data/')
    variable_type = type(hole_detection)
'''


#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe b, d, e, f, g', '\n')
class HoleDetection(Hole):
    def __init__(self, filename, filepath):
        """
        :param filename:
        :param filepath:
        """
        super().__init__()
        self._filepath = '../src_extern_data/'
        self._filename = None
        if type(filename) is str:
            self._filename = filename
        self._image = None
        self._hole_list = []

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if type(value) is str:
            self._filepath = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if type(value) is str:
            self._filename = value

    @property
    def image_path(self):
        image_path = self._filepath+self._filename
        return image_path

    @property
    def image(self):
        if self._image is None:
            img = cv2.imread(self.image_path, 1)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur_gray_image = cv2.medianBlur(gray_image, 5)
            self._image = blur_gray_image
            return self._image

    @property
    def hole_list(self):
        if not self._hole_list:
            some_holes = cv2.HoughCircles(self.image, cv2.HOUGH_GRADIENT, 1, 150,
                                          param1=500, param2=15, minRadius=0, maxRadius=50)
            for hole_radius in some_holes[0, :, 2]:
                hole_radius_mm = hole_radius / 75.6  # is the ratio of px / mm
                self._hole_list.append(Circle(radius=hole_radius_mm))
        return self._hole_list

    # ---------------- Methoden ------------------------

    def plot_radii(self):
        radius_holes = []
        for holes_nr in self.hole_list:
            radius_holes.append(holes_nr.radius)
        radius_holes.sort()

        radius_middle = [np.mean(radius_holes[0:6]),np.mean(radius_holes[7:13]),np.mean(radius_holes[14:20])]

        radius_holes = np.asarray(radius_holes)

        #-----------------------------------
        plt.figure(self._filename)
        plt.tight_layout(pad=1.5)
        plt.subplot(121)
        plt.hist(radius_holes, bins='auto', orientation='horizontal')
        plt.xlabel('No. of holes')
        plt.ylabel('Mittlerer Radius der Bohrgrößen in px')
        plt.yticks(radius_middle)

        plt.subplot(122)
        plt.plot(radius_holes, 'bo')
        plt.vlines([6.5, 13.5, 20.5], ymin=0.15, ymax=0.47, color='c',  linewidth=1, linestyle='-')
        plt.xlabel('No. of holes')
        plt.ylabel('Radius in px')
        plt.xlim((0, 25))
        plt.grid()
        plt.xticks(np.linspace(0, 25, 26))
        plt.show()
        pass




hole_detection = HoleDetection(filename='holes.JPG', filepath='../src_extern_data/')
hole_detection.plot_radii()








