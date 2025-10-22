class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self._prezzo = float(prezzo)
        self.disponibile = True
        self.passeggero = None

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = float(prezzo)

    def assegna(self, passeggero):
        if not self.disponibile:
            raise Exception(f"La cabina {self.codice} non è disponibile.")
        self.disponibile = False
        self.passeggero = passeggero

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile" + f" | Cliente --> {self.passeggero}"
        return f"{self.codice}: Base | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - {stato}"

    def __repr__(self):
        return f"[{self.__str__()}]"

    def __lt__(self, other):
        return self.prezzo < other.prezzo


class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, max_animali):
        super().__init__(codice, letti, ponte, prezzo)
        self.max_animali = int(max_animali)

    @property
    def prezzo(self):
        return self._prezzo * (1 + 0.1 * self.max_animali)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile" + f" | Cliente --> {self.passeggero}"
        return f"{self.codice}: Animali | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Max animali: {self.max_animali} - {stato}"


class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo)
        self.stile = stile

    @property
    def prezzo(self):
        return self._prezzo * 1.20

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile" + f" | Cliente --> {self.passeggero}"
        return f"{self.codice}: Deluxe | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo:.2f}€ - Stile: {self.stile} - {stato}"
