#########################################################################################
#                                                                                       #
#                                       WiSe 2324                                       #
#                       Simulation technischer Systeme mit Python                       #
#                                       Uebung 05                                       #
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
import copy
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
np.set_printoptions(suppress=True)
#########################################################################################

# ======================================= nächster Teil =================================
print(f'\n\n=========================\n||  Aufgabe 2.0  ||\n=========================\n')
# =======================================================================================
L = 150  # mm
Q = 3.4  # mm^2


def load(csv_number):
    data_name = 'Specimen_RawData_' + str(csv_number)
    folder = str('C:\\Users\\User\OneDrive\\Uni und Verbindung\\Uni und aktuelles Semester\\Aktuelles Semester\\WiSe 2324 - Simulation technischer Systeme mit Python\\Eigene Programme\\Simulation_mit_Python\\')
    data_path = folder + data_name + '.csv'

    file_read = None
    with open(data_path) as file_name:
        file_read = csv.reader(file_name)
        array = list(file_read)
    liste = array

    titles = str(array[4]).replace("'", "")
    titles = titles.replace("[", "")
    titles = titles.replace("]", "")
    titles = titles.replace(" ", "_")
    titles = titles.split(';')
    # print(titles)

    for i in range(1,7):
        del liste[0]

    # ---------------------------------------------------------------
    # Matrix erzeugen und negative Werte entfernen
    liste = umwandeln(liste)
    gereinigt = liste_bereinigen(liste)
    # print('\n\n')
    # print(gereinigt)
    # print('\n\n')

    # ---------------------------------------------------------------
    # Matrix in Dictionary umwandeln
    vorbereitung = np.transpose(gereinigt)
    dic = zip(titles,vorbereitung)
    dic = dict(dic)
    # print(dic)
    return dic
# ===================================================================


def umwandeln(array):
    zeilenzahl = len(array)
    matrix = []

    for i in range(zeilenzahl):
        zeile = array[i]
        spaltenzahl = len(zeile)

        werte = zeile[0]
        for j in range(1,spaltenzahl):
            werte += '.' + zeile[j]
        # print(werte)
        werte = werte.split(';')
        # print(werte)
        for j in range(len(werte)):
            werte[j] = float(werte[j])

        matrix.append(werte)
    return matrix
# ===================================================================


def liste_bereinigen(array):
    suchzeile = len(array)-1
    gefunden = 0
    for i in range(len(array)-1, -1, -1):
        beenden=False
        if array[i][3]>0:
            gefunden = suchzeile+1
            beenden = True
        if beenden: break
        else: suchzeile -=1

    new_array = copy.deepcopy(array[:gefunden])
    return new_array
# ===================================================================


def versagen(dic):
    y_max = max(dic["Last"])
    return y_max
# ===================================================================


def aus_gerade(dic):
    span = dic["Zugspannung"]
    dehn = dic["Dehnung_1"]
    slope, intercept = np.polyfit(dehn, span, 1)
    return
# ===================================================================


def main():
    Specimen_RawData_1 = load('1')
    Specimen_RawData_2 = load('2')
    Specimen_RawData_3 = load('3')
    Specimen_RawData_4 = load('4')
    Specimen_RawData_5 = load('5')

    datas = [Specimen_RawData_1, Specimen_RawData_2, Specimen_RawData_3, Specimen_RawData_4, Specimen_RawData_5]
    data_names = ['Specimen_RawData_1', 'Specimen_RawData_2', 'Specimen_RawData_3', 'Specimen_RawData_4', 'Specimen_RawData_5']
    # print(datas[0]['Zeit'])
    print(datas[0]['Zeit'][1])


    for i in [0,1,2,3,4]:
        print(data_names[i])
        for key, value in datas[i].items():
            print(key, ":", value, "\n")
        print('\n\n')

    print('\n\n===== Teilaufgabe 3 =====\n')
    plt.figure('Uebung 5 - Aufgabe 2.3')
    plt.subplot(211)
    plt.plot(Specimen_RawData_1["Traversenweg"], Specimen_RawData_1["Last"], color='b', label="Specimen_RawData_1", linewidth=2)
    plt.plot(Specimen_RawData_2["Traversenweg"], Specimen_RawData_2["Last"], color='c', label="Specimen_RawData_2", linewidth=2)
    plt.plot(Specimen_RawData_3["Traversenweg"], Specimen_RawData_3["Last"], color='r', label="Specimen_RawData_3", linewidth=2)
    plt.plot(Specimen_RawData_4["Traversenweg"], Specimen_RawData_4["Last"], color='g', label="Specimen_RawData_4", linewidth=2)
    plt.plot(Specimen_RawData_5["Traversenweg"], Specimen_RawData_5["Last"], color='k', label="Specimen_RawData_5", linewidth=2)

    pass


main()
# ======================================== Ende =========================================
print("                                    \n\n                                        ")
# =======================================================================================
# print (f'Weiter bei Aufgabe 0.0')