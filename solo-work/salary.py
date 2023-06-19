import csv

class Pracownik:
    def __init__(self, imie, nazwisko, pensja_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja_brutto

    def __str__(self):
        return self.imie + ' ' + self.nazwisko
    
    def oblicz_netto(self):
        podst_wym_skł_ub_zdr = self.pensja - (0.0976 + 0.015 + 0.0245) * self.pensja
        skł_ub_zdr = podst_wym_skł_ub_zdr * 0.09
        podst_ob_zal_pod_doch = podst_wym_skł_ub_zdr - 250
        zal_pod_doch = (0.12 * podst_ob_zal_pod_doch) - 300
        netto = round(podst_wym_skł_ub_zdr - skł_ub_zdr - zal_pod_doch,2)
        return netto
    
    def oblicz_koszty_pracodawcy(self):
        koszty_pracodawcy = round(self.pensja + self.pensja * (0.0976 + 0.065 + 0.0167 + 0.0245 + 0.001),2)
        return koszty_pracodawcy
    
    def wygeneruj_raport(self):
        print("Wynagrodzenie zasadnicze: " + str(self.pensja))
        print("Składka na ubezpieczenia społeczne: " + str(round((0.0976 + 0.015 + 0.0245) * self.pensja,2)))
        print("Składka na ubezpieczenie zdrowotne: " + str(round(((self.pensja - (0.0976 + 0.015 + 0.0245) * self.pensja)) * 0.09,2)))
        print("Zaliczka na podatek dochodowy: " + str(round(0.12 * ((self.pensja - (0.0976 + 0.015 + 0.0245) * self.pensja)  - 250) - 300,2)))
        print("Wynagrodzenie netto: " + str(round(self.oblicz_netto(),2)))

pracownik1 = Pracownik("Jan", "Kowalski", 3500)

pracownik1.wygeneruj_raport()

print(pracownik1)
print(pracownik1.oblicz_netto())
print(pracownik1.oblicz_koszty_pracodawcy())
    
assert pracownik1.oblicz_netto() == 2715.92
assert pracownik1.oblicz_koszty_pracodawcy() == 4216.8

with open("solo-work/data/pracownicy.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        pracownik = Pracownik(row[0], row[1], int(row[2]))
        print(pracownik)
        print(pracownik.oblicz_netto())
        print(pracownik.oblicz_koszty_pracodawcy())
        
