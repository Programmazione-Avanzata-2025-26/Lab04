import csv
from passeggero import Passeggero
from cabine import *

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.cabine = []
        self.passeggeri = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        self.cabine.clear()
        self.passeggeri.clear()

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if not row:
                        continue
                    codice = row[0]
                    if codice.startswith("CAB"):
                        # Gestione cabine
                        if len(row) == 4: # Cabina Base
                            cabina = Cabina(*row) # uguale a "Cabina(row[0], row[1], row[2], row[3])"
                        elif len(row) == 5: # Cabina Animali o Deluxe
                            # Se è numerico -> cabina animali, se no deluxe
                            if row[4].isdigit():
                                cabina = CabinaAnimali(row[0], row[1], row[2], row[3], row[4])
                            else:
                                cabina = CabinaDeluxe(row[0], row[1], row[2], row[3], row[4])
                        self.cabine.append(cabina)
                    elif codice.startswith("P"):
                        nome, cognome = row[1:]
                        passeggero = Passeggero(codice, nome, cognome)
                        self.passeggeri.append(passeggero)
        except FileNotFoundError:
            raise FileNotFoundError("Il file CSV non è stato trovato.")

    def _trova_cabina(self, codice):
        return next((c for c in self.cabine if c.codice == codice), None)

    def _trova_passeggero(self, codice):
        return next((p for p in self.passeggeri if p.codice == codice), None)

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        cabina = self._trova_cabina(codice_cabina)
        passeggero = self._trova_passeggero(codice_passeggero)

        if not cabina:
            raise Exception("Cabina non trovata.")
        if not passeggero:
            raise Exception("Passeggero non trovato.")
        if not cabina.disponibile:
            raise Exception("Cabina non disponibile.")
        for c in self.cabine:
            if passeggero == c.passeggero:
                raise Exception("Passeggero già associato ad una cabina.")

        cabina.assegna(passeggero)

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # SOLUZIONE 1: definire il metodo __lt__() dentro la classe Cabina quindi usare un "sorted()"
        return sorted(self.cabine)

        # SOLUZIONE 2: Usare il metodo con la lista di tuple temporanea vista nel lab03
        # temp = [(c.prezzo, c) for c in cabine]
        # temp.sort()  # ordina in base al prezzo
        # cabine_sorted = [c for _, c in temp]

        # SOLUZIONE 3: return sorted(self.cabine, key=attrgetter('prezzo')) con "from operator import attrgetter"

        # SOLUZIONE 4: return sorted(self.cabine, key=lambda c: c.prezzo)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.passeggeri:
            res = f"- {p}"
            for c in self.cabine:
                if p == c.passeggero: # Affinché questo funzioni deve essere definito il metodo __eq__() nella classe Passeggero
                    res = f"{res} --> Assegnato alla cabina: {c.codice}"
                    break
            print(res)
