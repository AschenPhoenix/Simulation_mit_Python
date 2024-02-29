"""
Module description
@date: 
@author: Hendrik Traub <h.traub@tu-bs.de>
@Copyright: 2020 TU Braunschweig
<www.tu-braunschweig.de>. All rights reserved.
"""
import datetime
import numpy as np


class Impfpass:
    def __init__(self):
        self._geimpft = False
        self._genesen = False
        self._getestet = datetime.datetime.now() - datetime.timedelta(hours=25)

    def set_geimpft(self):
        self._geimpft = True

    def set_genesen(self):
        self._genesen = True

    def set_getestet(self):
        self._getestet = datetime.datetime.now()

    def einlass_erlaubt(self):

        now = datetime.datetime.now()
        time_since_last_test = now - self._getestet
        max_time_difference = datetime.timedelta(hours=24)
        last_test_less_one_day = time_since_last_test < max_time_difference

        einlass_erlaubt = self._geimpft or self._genesen
        einlass_erlaubt = einlass_erlaubt or last_test_less_one_day

        return einlass_erlaubt


def create_customers(size):
    """
    Gibt eine Liste mit Impfpässen zurück
    :param size: Anzahl der Impfpässe
    :return: customers: list(Impfpass)
    """
    #  Zufallszahlen
    geimpft = np.random.randint(2, size=size)
    getestet = np.random.randint(2, size=size)
    genesen = np.random.randint(2, size=size)

    customers = []
    for impf, test, nesen in zip(geimpft, getestet, genesen):
        person = Impfpass()
        if impf:
            person.set_geimpft()
        if test:
            person.set_getestet()
        if nesen:
            person.set_genesen()

        customers.append(person)

    return customers

