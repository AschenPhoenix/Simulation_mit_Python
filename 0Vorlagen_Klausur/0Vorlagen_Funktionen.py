# ##################################################################################################################
# Erstellen eines Dictionarys
    dic1 = {'Para_1': [1,2,3], 'Para_2': [4,5,6]}
    # oder
    dic2 = dict(Para_3=[1,2,3], Para_4=[4,5,6])
# Erweitern eines Dictionarys
    dic2['Para_5'] = [7,8,9]

# Erstellen voon Dictionarys mit Unterkapiteln
    dic3={}
    dic3['Kapitel_1'] = {'Para_1':1,'Para_2':2}
    dic3['Kapitel_2'] = {'Para_3':3,'Para_4':4}

# Dictionarys zusammenfügen
    dic4={}
    dic4.update(dic1)
    dic4.update(dic2)
    # oder durch Neuerstellung
    dic5 = dict(dic1, **dic2)

# Ausgeben der daten eines Dictionarys auf schöne Weise
    dictionary_name = dic1
    for key, value in dictionary_name.items():
        print(key, f":\t", value)

    dictionary_name = dic5
    for key1, value1 in dictionary_name.items():
        print(key1.replace('\n', ''))
        for key2, value2 in value1.items():
            print(f" \t", key2, f":\t", value2)
        print('  ')

# ##################################################################################################################
# plot mit zwei y-Achsen
    fig, ax1 = plt.subplots()

    # linke Y-Achse
    pl1=ax1.plot()
    ax1.set_ylim([0,0])
    ax1.set_ylabel('0', color='blue')

    ax1.set_ylim([0,0])
    ax1.set_ylabel('0', color='blue')

    # rechte Y-Achse
    ax2 = ax1.twinx()
    pl2=ax2.plot()
    ax2.set_xlim([0,0])
    ax2.set_xlabel('0')

# ##################################################################################################################
# Normalverteilung, Mittelwert, Standartabweichung
    array1 = sigma*np.random.randn(n)+mittelwert  # 1D Array beliebiger Größe mit Normalverteilten Einträgen mit
                                                  # beliebigen Mittelwerten und Standardabweichungen
    mean = np.mean(array1)  # Funktion zur Berechnung des Mittelwertes eines Arrays
    std = np.std(array1)  # Funktion zur Berechnung der Standartabweichung eines Arrays

# ##################################################################################################################
# Lösen eines linearen Gleichungssystems
    '''Lineares Gleichungssystem Lösen
    __________________________________
    1*x1 + 2*x2 = 5
    3*x1 + 4*x2 = 11
    
    ges: x=[x1 x2]'''

    A=np.array([[1,2],[3,4]])
    b=np.array([[5],[11]])

    y=np.linalg.solve(A,b)  # Anwendbar, solange die Inverse der Matrix A berechnet werden kann.
    np.linalg.inv(A)        # Berechnet die Inverse der Matrix A.
    np.linalg.pinv(A)       # Berechnet die Pseudo-Inverse der Matrix A. Zum Beispiel dann,
                            # wenn A nicht quadratisch oder eine singuläre Matrix ist.
    np.linalg.lstsq(A,b)    # Berechnet eine Annäherung der Lösung x für das unlösbare lineare Gleichungssysteme.
                            # Die Lösung ist dann aber Fehlerbehaftet im Sinne der Methode der kleinsten Quadrate
                            # und stellt eine Annäherung der Lösung dar.

    def dgl_pruefen(A,b):
        try:
            if np.linalg.det(A) != 0:
                print("Das Gleichungssystem ist lösbar")
                x = np.linalg.solve(A, b)
                print(f"Die Lösung lautet:\n{x}\n")
            else:
                print("Das Gleichungssystem ist nicht lösbar")
                x = np.linalg.lstsq(A, b, rcond=None)
                print(f"Die Annäherungslösung lautet:\n{x[0]}\n")
        except:
            print("Das Gleichungssystem ist nicht lösbar")
            x = np.linalg.lstsq(A, b, rcond=None)
            print(f"Die Annäherungslösung lautet:\n{x[0]}\n")


# ##################################################################################################################
# Interpolieren
    x=np.linspace(0,2*np.pi, 8)
    x2=np.linspace(0,2*np.pi, 80)

    y=np.sin(x)
    y2=np.sin(x2)

    f= interp1d(x,y,kind='linear')
    print(f,'\n')

    fx2 = f(x2)
    print(fx2,'\n')

    diff =abs(y2-fx2)
    max_diff = max(diff)
    print('Maximale Differenz: ',max_diff)


# ##################################################################################################################
# Anonyme-Funktionen
    f=lambda x:x**2.+4
    val=f(2)
    print('val= %20.2f' %val)


# ##################################################################################################################
#



# ##################################################################################################################
#
