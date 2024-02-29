# Das ist ein Kommentar und wird vom Interpreter ignoriert
# ------------------------
print('----==== Programm Start ====----')
# ------------------------
# Berechnung
x=(27*3)**0.5
y= 3.14159265359

# ------------------------
# (1.0) Ausgabe der Ergebnisse
print('x=', x, 'y=', y)
#  ------------------------
# (1.1) %-formatting, Ausgabe der Ergebnisse
print('x=%f y=%f'%(x,y)) # Ausgabe ohne Formatvorlage
# ------------------------
# (1.2) str.format(), Ausgabe der Ergebnisse
print('x={}, y={}'.format(x,y))
# ------------------------
# (1.3) f-Strings, Ausgabe der Ergebnisse
print(f'x={x}, y={y}')

# ------------------------
# (2.0) %-formatting, Formatierte Ausgabe der Ergebnisse
print('x=%4.2f y=%4.2f'%(x,y)) # Ausgabe mit Formatvorlage
# ------------------------
# (2.1) str.format(), Formatierte Ausgabe der Ergebnisse
print('x={:5.2f}, y={:.10}'.format(x,y))
# ------------------------
# (2.2) f-Strings, Formatierte Ausgabe der Ergebnisse
print(f'x={x:5.3}, y={y:.7}')
# ------------------------
# Löschen der verwendeten Variablen
del x,y
print('----==== Programm Ende ====----')


#########################################################################################

