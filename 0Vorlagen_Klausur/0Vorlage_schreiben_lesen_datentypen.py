# ##################################################################################################################
# txt Datei lesen
datapath = folderpath+'\\'+datanamelist[n]
datafile = open(datapath,'r')
data = []
for line in datafile:
    data.append(line)
datafile.close()

# =======================================================
# txt Datei schreiben
data = open(r'../src_extern_data/u6_a4_export.txt','w')
data.write('Datenexport - Übung 6 - Aufgabe 4\n')
data.write('Anregungsfrequenz:\t10\trad/s\n\n')
data.write('\tZeit\t\tx1(t)\t\tx1p(t)\t\tx2(t)\t\tx2p(t)\t\tx3(t)\t\tx3p(t)\n')
for n in range(len(sol.t)):
    data.write(f'{sol.t[n]:10.3}\t{sol.y[0][n]:10.3}\t{sol.y[1][n]:10.3}\t{sol.y[2][n]:10.3}\t{sol.y[3][n]:10.3}\t{sol.y[4][n]:10.3}\t{sol.y[5][n]:10.3}\n')
data.close()

# ##################################################################################################################
# csv Datei lesen (auch verwenden, wenn exel gewünscht)
path = r'../src_extern_data/u6_a5_export.csv'
csv_zugversuch = []
with open(path) as csv_data:
    csv_read = csv.reader(csv_data, delimiter=';')
    for row in csv_read:
        csv_zugversuch.append(row)
csv_data.close()

# =======================================================
# csv Datei schreiben (auch verwenden, wenn exel gewünscht)
file = open(r'../src_extern_data/u6_a5_export.csv','w')
file.write('Time; Amplitude\n')
for i in range(0,len(sol.t)):
    file.write(str(sol.t[i])+';'+str(sol.y[0][i])+'\n')
file.close()

# =======================================================
# xlsx Datei lesen (nur lesen!)
filename = "../src_extern_data/MeineDaten.xlsx"
file = opx.load_workbook(filename)
data = file['Tabelle1']
l = len(data['A'])

Daten = {data['A1'].value: [], data['B1'].value: [], data['C1'].value: []}
for i in range(2,l):
    Daten[data['A1'].value].append(float(data['A' + str(i)].value))
    Daten[data['B1'].value].append(float(data['B' + str(i)].value))
    Daten[data['C1'].value].append(float(data['C' + str(i)].value))
for key, value in Daten.items():
    print(key, f":\t", value)
file.close()

# ##################################################################################################################
