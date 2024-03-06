# Einlesen einer CSV-Datei
def einlesen_csv(path):
    csv_zugversuch = []
    with open(path) as csv_data:
        csv_read = csv.reader(csv_data, delimiter=';')
        for row in csv_read:
            csv_zugversuch.append(row)
    csv_data.close()
    return csv_zugversuch


# ##################################################################################################################
# Einlesen einer txt-Datei
def einlesen_txt(path):
    datafile = open(path, 'r')
    data = []
    for line in datafile:
        data.append(line)
    datafile.close()
    return data


# ##################################################################################################################
# Einlesen einer xlsx-Datei und speichern als Dictionary
def einlesen_xlsx(path):
    import openpyxl as opx
    file = opx.load_workbook(path)
    data = file['Tabelle1']
    file.close()

    l = len(data['A'])

    Daten = {data['A1'].value: [], data['B1'].value: [], data['C1'].value: []}
    for i in range(2, l):
        Daten[data['A1'].value].append(float(data['A' + str(i)].value))
        Daten[data['B1'].value].append(float(data['B' + str(i)].value))
        Daten[data['C1'].value].append(float(data['C' + str(i)].value))
    # for key, value in Daten.items():
    #    print(key, f":\t", value)
    return Daten


# ##################################################################################################################
# Einlesen eines Images
def einlesen_json(image_path):
    import cv2
    img = cv2.imread(image_path, 1)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_gray_image = cv2.medianBlur(gray_image, 5)
    image = blur_gray_image
    return image


# ##################################################################################################################












