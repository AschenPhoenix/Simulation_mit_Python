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
    csv_data.close()
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
        dehnung.append(float(werte[m][3])*1e-2)
        spannung.append(float(werte[m][4])*1e-3)

    # Finden der Fehlerdaten
    found = []
    l = len(dehnung)
    for k in range(l-1,0,-1):
        if not found and dehnung[k] >= 0:
            found.append(k+1)

    # Entfernen der Fehlerhaften Daten
    for j in range(l-1, found[0], -1):
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
            f_l.append(k-1)
            f_l.append(k)
        if not f_u and dehn[k] >= 0.0025:
            f_u.append(k - 1)
            f_u.append(k)

    diff_l = (dehn[f_l[1]]-0.0005)/(dehn[f_l[1]]-dehn[f_l[0]])
    span_l = (span[f_l[1]]-span[f_l[0]])*diff_l
    diff_u = (dehn[f_u[1]] - 0.0025) / (dehn[f_u[1]] - dehn[f_u[0]])
    span_u = (span[f_u[1]] - span[f_u[0]]) * diff_u

    e_mod = np.polyfit([0.0005,0.0025],[span_l,span_u],1)
    e_mod[1] = e_mod[1]/1e9

    # Berechnung Versagenslast
    v_lasten = np.max(lasten)

    return e_mod, v_lasten

# ------------- Dictionary Erstellung -----------------------------
def dic_anlegen(daten_pfad,p_laenge, p_flaeche):
    dic = {}
    #print(len(daten_pfad))
    for n in range(len(daten_pfad)):
        # Datenentnahme und Verarbeitung
        v_daten = einlesen(daten_pfad[n])
        v_name, v_date_time, v_para, value = zerlegen(v_daten)
        zeit, weg, last, dehnung, spannung = datenbereinigung(value)
        e_modul, ver_last = parameter_berechnung(dehnung, spannung, last)
        # Unterkapitel anlegen
        dic['Versuch_' + str(n+1)] = {'Probenbeschriftung': v_name,
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
def versuch_plotten(dictionary, anz):
    e_modulos = []
    v_lasten = []
    s = []
    f = []
    dehn = []
    span = []

    for n in range(anz):
        s.append(dictionary['Versuch_' + str(n+1)]['Traversenweg'])
        f.append(dictionary['Versuch_' + str(n+1)]['Last'])
        span.append(dictionary['Versuch_' + str(n+1)]['Zugspannung'])
        e_modulos.append(dictionary['Versuch_' + str(n+1)]['E-Modul'])
        v_lasten.append(dictionary['Versuch_' + str(n+1)]['Versagenslast'])
        d=[]
        for m in range (len(dictionary['Versuch_' + str(n+1)]['Dehnung_1'])):
            d.append(dictionary['Versuch_' + str(n+1)]['Dehnung_1'][m]*100)
        dehn.append(d)

    plt.figure()
    plt.subplot(221)
    plt.title('Kraft-Weg-Diagramm')
    for m in range(anz):
        plt.plot(s[m][:], f[m][:], '-', label=f'Zugversuch_'+str(m+1))
    #plt.xlim([0,4])
    #plt.ylim([0,7500])
    plt.xlabel('Traversenweg in [m]')
    plt.ylabel('Kraft in [N]')
    plt.legend(loc='lower right')
    plt.grid()

    plt.subplot(222) # In Lösung verwenden sie nur die Dehnung
    plt.title('Spannung-Dehnung-Diagramm')
    for m in range(anz):
        plt.plot(dehn[m][:], span[m][:], '-', label=f'Zugversuch_' + str(m + 1))
        e_m_plot = [[dehn[m][0],np.max(dehn[m][:])], [np.min(span[m][:]), (np.min(span[m][:])+(max(dehn[m][:]) - dehn[m][0])*e_modulos[m][0])]]
        plt.plot(e_m_plot[0][:],e_m_plot[1][:],'--', label=f'Ausgleichsgerade V' + str(m+1))
    #plt.xlim([-0.1, 2.7])
    #plt.ylim([-0.1, 2.7])
    plt.xlabel('Dehnung in [%]')
    plt.ylabel('Spannung in [GPa]')
    plt.legend(loc='lower right')
    plt.grid()

    plt.subplot(223)
    plt.title('E-Module in [GPa]')
    e_modul = []
    for k in range(anz):
        e_modul.append(e_modulos[k][1])
    plt.hist(e_modul)

    plt.subplot(224)
    plt.title('E-Module in [GPa]')
    plt.hist(v_lasten)
    plt.show()


# ------------- Start -----------------------------
L = 150  # mm
A = 3.45  # mm^2
anzahl_Versuchsdateien = 5
versuch_path = []
folder_path = '../src_extern_data/'

for n in range(anzahl_Versuchsdateien):
    versuch_path.append(folder_path + 'Specimen_RawData_' + str(n+1) + '.csv')
print(versuch_path)

Zugversuche = dic_anlegen(versuch_path,L,A)
for key1, value1 in Zugversuche.items():
    print(key1.replace('\n', ''))
    for key2, value2 in value1.items():
        print(f" \t", key2, f":\t", value2)
    print('  ')
versuch_plotten(Zugversuche, anzahl_Versuchsdateien)



#daten = einlesen(versuch_path[0])
#print(daten)
#dic_name, dic_date_time, dic_para, values = zerlegen(daten)
#print(values)




