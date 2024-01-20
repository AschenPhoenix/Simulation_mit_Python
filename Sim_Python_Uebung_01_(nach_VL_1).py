#
#               WiSe 2324 - Simulation technischer Systeme mit Python
#                               Übung 01
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
#========================= Teil 01 =====================================
print(f'\n\n=====================\n||   Aufgabe 1+2   ||\n=====================\n')
# Aufgabe 1 und 2 übersprrungen
x=[0,1,2,3,4,5,6,7,8,9,10] 
print(f'{float(x[0]):04.1f} | {float(x[2]):04.2f} | {float(x[4]):04.1f} | {float(x[6]):04.1f} | {float(x[8]):04.1f} | {float(x[10]):04.1f} | ')

#======================================== Teil 03 =================================
print(f'\n\n=====================\n||   Aufgabe 0.1   ||\n=====================\n')
#==================================================================================


MyText="Python ist eine universelle, üblicherweise interpretierte hö-here Programmiersprache. Sie hat den Anspruch, einen gut lesbaren, knappen Programmierstil zu fördern. So werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch Einrückungen struktu-riert. Wegen seiner klaren und übersichtlichen Syntax gilt Python als einfach zu erlernen. Python unterstützt mehrere Programmierparadigmen, z.B. die objektorientierte, die aspektorientierte und die funktionale Programmierung. Ferner bietet es eine dynamische Typisierung. Wie viele dynamische Sprachen wird Python oft als Skriptsprache genutzt. Die Sprache weist ein offenes, gemeinschaftsbasiertes Entwicklungsmodell auf, das durch die gemeinnützige Python Software Foundation gestützt wird, die de facto die Definition der Sprache in der Referenzumsetzung CPython pflegt."

MySearch=input("Stichwort für die Suche: \n") 
Location=MyText.find(MySearch)  # Gibt aus, ob das Stichwort in dem text gefunden wurde und wo es das erste mal auftritt. Wird nichts gefunden, gibt es -1 als Wert aus.
Counts=MyText.count(MySearch)   # Gibt aus, wie oft das wort im Text vorkommt.

if Location>=0: 
    print(f'Das Stichwort: \"{MySearch}\" wurde {Counts}-mal gefunden\nerste Fundstelle: {Location}') 
else: 
    print(f'Das Stichwort: \"{MySearch}\" wurde nicht gefunden')



#======================================== Teil 03 =================================
print(f'\n\n=====================\n||   Aufgabe 3.2   ||\n=====================\n')
#==================================================================================
name = input('Wie lautet dein Name?\n') 
sprache = input('\nWas ist deine Lieblingssprache?\n') 
print('\n\n')
if sprache =='deutsch': 
    print('Hallo ' + str(name) + '!') 
elif sprache =='englisch': print('Hello ' + str(name) + '!') 
elif sprache == 'spanisch': print('¡Hola ' + str(name) + '!') 
elif sprache == 'chinesisch': print('Ni hao ' + str(name) + '!') 
elif sprache == 'japanisch': print('Kon\'nichiwa ' + str(name) + '!') 
elif sprache == 'arabisch': print('Marhabaan ' + str(name) + '!') 
elif sprache == 'hindi': print('Abhinandan ' + str(name) + '!') 
else: print('Diese Sprache kenne ich noch nicht')

#======================================== Teil 03 =================================
print(f'\n\n=====================\n||   Aufgabe 3.3   ||\n=====================\n')
#==================================================================================
print('---------------------------') 
print("----- { Zahlenraten } -----\nVersuche mit möglichst wenig\nver-suchen die unbekannte Zahl\nzu erraten") 
print() 
a=10 
b=float(input("Rate die Zahl:\n")) 
if a<b: print("Die Zahl ist zu groß!") 
elif a>b: print("Die Zahl ist zu klein!") 
elif a==b: 
    print('* + * + * + * + * + * + *') 
    print("GEWONNEN! Du hast die Zahl erraten!") 
    print('* + * + * + * + * + * + *') 
print() 
print('----- { Spiel Ende } -----') 
print('---------------------------')

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||   Aufgabe 4.1   ||\n=====================\n')
#==================================================================================
zahlen=[0,1,2,3,4,5,6,7,8,9,10]
for i in zahlen:
    print(f'{i}')

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||   Aufgabe 4.2   ||\n=====================\n')
#==================================================================================
liste=[]
for n in range(10+1):
    liste.append(n)
    print(f'{liste}')

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||   Aufgabe 4.4   ||\n=====================\n')
#==================================================================================
x=[2,4,1,7,6,10,9,5,3,8]
print(f'x={x}')
x.sort()
print(f'x={x}')

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||   Aufgabe 4.3   ||\n=====================\n')
#==================================================================================
MyText="Python ist eine universelle, üblicherweise interpretierte hö-here Programmiersprache. Sie hat den Anspruch, einen gut lesbaren, knappen Programmierstil zu fördern. So werden beispielsweise Blöcke nicht durch geschweifte Klammern, sondern durch Einrückungen struktu-riert. Wegen seiner klaren und übersichtlichen Syntax gilt Python als einfach zu erlernen. Python unterstützt mehrere Programmierparadigmen, z.B. die objektorientierte, die aspektorientierte und die funktionale Programmierung. Ferner bietet es eine dynamische Typisierung. Wie viele dynamische Sprachen wird Python oft als Skriptsprache genutzt. Die Sprache weist ein offenes, gemeinschaftsbasiertes Entwicklungsmodell auf, das durch die gemeinnützige Python Software Foundation gestützt wird, die de facto die Definition der Sprache in der Referenzumsetzung CPython pflegt."

MySearch=input("Stichwort für die Suche: \n") 
Counts=MyText.count(MySearch)   # Gibt aus, wie oft das wort im Text vorkommt.
len_=len(MyText)
Locations=[MyText.find(MySearch)]
for n in range(0,Counts):  # Gibt aus, ob das Stichwort in dem text gefunden wurde und sich alle befinden. Wird nichts gefunden, gibt es -1 als Wert aus.
    Location=MyText.find(MySearch)
    neu=Location+Locations[-1]
    Locations.append(neu)
if Counts!=0: 
    print(f'Das Stichwort: \"{MySearch}\" wurde {Counts}-mal gefunden\nVollgende Fundstelle (Zeichenstellen): {Locations}') 
else: 
    print(f'Das Stichwort: \"{MySearch}\" wurde nicht gefunden')

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||   Aufgabe 4.5   ||\n=====================\n')
#==================================================================================
cryptList = ['die', 'ist', 'Auf', 'ist', 'und', 'wichtigen', 'einem', 'Quelltext', 'für', 'objektori-entierten', 'abstrakten', 'und', 'zusätzliche', 'Anwendungsentwicklung', 'und', 'sowie', 'Skripte', 'Programmierung.', 'in', 'Programmiersprache', 'der', 'sowohl', 'mächtige', 'auf', 'für', 'binärer', 'umfangreiche', 'aber', 'Form', 'aber', 'Achtung!', 'einfach', 'eine', 'Syntax', 'als', 'tolle', 'gleichen', 'und', 'die', 'Sei te', 'für', 'mit', 'http://www.python.org', 'freie', 'elegante', 'Der', 'geeignet.', 'sind', 'Development)', 'auch', 'effizienten', 'von', 'Ap-plication', 'Verweise', 'alle', 'Sprache', 'Standardbibliothek', 'Werkzeuge,', 'Distributio-nen', 'finden', 'schnelle', 'und', 'als', 'weiterverbreitet', 'hervorragend', 'Typisierung', '(Rapid', 'Drittanbietern,', 'Geheim!', 'auf', 'Ansatz', 'und', 'frei', 'Programme', 'verfüg-bar,', 'werden.', 'Python', 'Module,', 'Python', 'einfachen,', 'als', 'dynamische', 'frei', 'die', 'Dokumentation.', 'lernende,', 'Webseite', 'Python-Interpreter', 'zu', 'interpretierte', 'können', 'zur', 'der', 'sich', 'Plattformen', 'weitere', 'effektiven', 'Durch', 'Datenstruk-turen']
key=[30, 68, 78, 3, 32, 35, 19]
n=0
for n in range(0,len(key)):
    print(f'{cryptList[key[n]]}')
    n+=1

#======================================== Teil 04 =================================
print(f'\n\n=====================\n||   Aufgabe 4.6   ||\n=====================\n')
#==================================================================================
f=[0,1]
while len(f)<100:
    neu=(f[-1]+f[-2])
    f.append(neu)
x=list(range(1,101))
plt.plot(x,f)
plt.xscale("log")
plt.yscale("log")
plt.title("Uebung 1 - Aufgabe 4.6 (Fibonacci-Folge)")
plt.show()

#======================================== Teil 05 =================================
print(f'\n\n=====================\n||   Aufgabe 5.3   ||\n=====================\n')
#==================================================================================
while true:
    print('---------------------------') 
    print("----- { Zahlenraten } -----\nVersuche mit möglichst wenig\nversuchen die unbekannte Zahl\nzu erraten") 
    print() 
    a=10 
    b=float(input("Rate die Zahl:\n")) 
    if a<b: print("Die Zahl ist zu groß!") 
    elif a>b: print("Die Zahl ist zu klein!") 
    elif a==b: 
        print('* + * + * + * + * + * + *') 
        print("GEWONNEN! Du hast die Zahl erraten!") 
        print('* + * + * + * + * + * + *')
        break 
    print("\n")
    frage=input("Möchtest du weiter Spielen?\n(Wenn du weiter spielen möchtest, antworte mit \"1\")\n(Wenn du nicht weiter spielen möchtest, antworte mit \"0\")\nAntwort: ")
    if int(frage)==0.0: break
print('\n\n---------------------------') 
print('----- { Spiel Ende } -----') 
print('---------------------------')

#========================== Ende =======================================
print("\n\n")
#=======================================================================