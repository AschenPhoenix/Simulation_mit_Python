class Klasse_1:
    """
    Klasse_1 für ...
    """
    # Klassenattribute
    para_1 = 0
    class_counter = 0

    def __init__(self, value1, value2):
        """
        Initialisation der Klasse_1
        :param value1:
        :param value2:
        """
        self.value1 = 0
        self.value1 = value1
        self._value2 = 0
        self.value2 = value2

    @property
    def value2(self):
        # Zum Erstellen von Protected Values
        return self._value2

    @value2.setter
    def value2(self, value):
        # Zum Setzen von geschützten Variablen
        self.value2 = value/2

    def klassenmethode(self, value1, value2):
        """
        Methode mit der Aufgabe ...
        :param value1:
        :param value2:
        :return:
        """
        print("Klassenparameter", value1, value2)


# ##################################################################################################################
class UnterKlasse_1:
    def __init__(self, value3, value4):
        """
        Initialisation der UnterKlasse_1
        :param value3:
        :param value4:
        """
        super().__init__()
        self.value1 = 0
        self.value3 = value3
        self._value4 = 0
        self._value4 = value4

    @property
    def value4(self):
        # Zum Erstellen von Protected Values
        return self._value4

    @value4.setter
    def value4(self, value):
        # Zum Setzen von geschützten Variablen
        self._value4 = value / self.value1  # Zugriff auf Variablen aus Oberklasse möglich

