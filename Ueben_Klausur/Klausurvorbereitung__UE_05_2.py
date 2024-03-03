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
mplt.use('Qt5Agg')
np.set_printoptions(suppress=True)
#plt.tight_layout(pad=0.5)




#########################################################################################
print('\n\n\n', '\t\t\t Aufgabe 2.0', '\n')

# ------------- Funktionen -----------------------------
def einlesen(path):
    csv_zugversuch = []
    with open(path) as csv_data:
        csv_read = csv.reader(csv_data, delimiter=';')
        for row in csv_read:
            csv_zugversuch.append(row)
    return csv_zugversuch

def zerlegen(data):
    head = data[0:5]
    values = data[6:]

    dic_name = head[0][1]
    dic_date_time = str(head[1][1])
    dic_para = [str(head[4][0]),
                str(head[4][1]),
                str(head[4][2]),
                str(head[4][3]).replace(' ', '_'),
                str(head[4][4])]
    return dic_name, dic_date_time, dic_para, values

def datenbereinigung(values):
    zeit = []
    weg = []
    last = []
    dehnung = []
    spannung = []

    # Strukturanpassung
    werte = values
    for m in range(len(values)):
        for n in range(5):
            werte[m][n] = werte[m][n].replace(',', '.')
        zeit.append(float(werte[m][0]))
        weg.append(float(werte[m][1])*1e3)
        last.append(float(werte[m][2])*1e-3)
        dehnung.append(float(werte[m][3]))
        spannung.append(float(werte[m][4])*1e-3)

    # Finden der Fehlerdaten
    found = []
    for k in range(len(dehnung)-1,0,-1):
        if not found and dehnung[k] >= 0:
            found.append(k+1)

    # Entfernen der Fehlerhaften Daten
    for j in range(found[0], len(dehnung)):
        del zeit[j]
        del weg[j]
        del last[j]
        del dehnung[j]
        del spannung[j]

    return zeit, weg, last, dehnung, spannung

def parameter_berechnung(dehn, span, lasten):
    # Berechnung E-Modul
    f_l = []
    f_u = []
    for k in range(0,len(dehn)):
        if not f_l and dehn[k] >= 0.0005:
            f_l.append([k-1,k])
        if not f_u and dehn[k] >= 0.0025:
            f_u.append([k-1,k])

    diff_l = (dehn[f_l[1]]-0.0005)/(dehn[f_l[1]]-dehn[f_l[0]])
    span_l = (span[f_l[1]]-span[f_l[0]])*diff_l
    diff_u = (dehn[f_u[1]] - 0.0025) / (dehn[f_u[1]] - dehn[f_u[0]])
    span_u = (span[f_u[1]] - span[f_u[0]]) * diff_u

    e_mod = np.polyfit([0.0005,0.0025],[span_l,span_u])

    # Berechnung Versagenslast
    v_lasten = np.max(lasten)

    return e_mod, v_lasten

# ------------- Dictionary Erstellung -----------------------------
def dic_anlegen(daten_pfad,p_laenge, p_flaeche):
    dic = {}
    for n in range(len(daten_pfad)):
        # Datenentnahme und Verarbeitung
        v_daten = einlesen(daten_pfad[0])
        v_name, v_date_time, v_para, value = zerlegen(v_daten)
        zeit, weg, last, dehnung, spannung = datenbereinigung(value)
        e_modul, ver_last = parameter_berechnung(dehnung, spannung, last)
        # Unterkapitel anlegen
        dic['Versuch_' + str(n)] = {'Probenbeschriftung': v_name,
                                    'Versuchsdatum': v_date_time,
                                    'Proben-Laenge': p_laenge,
                                    'Proben-Querschnittsflaeche': p_flaeche,
                                    v_para[0]: zeit,
                                    v_para[1]: weg,
                                    v_para[2]: last,
                                    v_para[3]: dehnung,
                                    v_para[4]: spannung,
                                    'E-Modul': e_modul,
                                    'Versagenslast': ver_last}
    return dic

# ------------- Plot-Funktion -----------------------------
def versuch_plotten():



# ------------- Start -----------------------------
L = 150  # mm
A = 3.45  # mm^2
anzahl_Versuchsdateien = 1
versuch_path = []
folder_path = '../src_extern_data/'

for n in range(1, anzahl_Versuchsdateien + 1):
    versuch_path.append(folder_path + 'Specimen_RawData_' + str(n) + '.csv')

Zugversuche = dic_anlegen(versuch_path,L,A)




#daten = einlesen(versuchsdaten_list[0])
#print(daten)
#dic_name, dic_date_time, dic_para, values = zerlegen(daten)
#print(values)




