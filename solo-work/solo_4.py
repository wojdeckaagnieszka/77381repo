class Mieszkanie:
    def __init__(self, powierzchnia_mkw, liczba_pokoi, pietro, miasto, dzielnica, rynek, cena, czynsz):
        self.powierzchnia_mkw = powierzchnia_mkw
        self.liczba_pokoi = liczba_pokoi
        self.pietro = pietro
        self.miasto = miasto
        self.dzielnica = dzielnica
        self.rynek = rynek
        self.cena = cena
        self.czynsz = czynsz
        self.sklepy = []

    def __str__(self):
        return "Mieszkanie " + str(self.powierzchnia_mkw) + " mkw " + self.miasto

    def oblicz_cene_mkw(self):
        cena_mkw = self.cena/self.powierzchnia_mkw
        return cena_mkw
    
    def dodaj_sklepy_w_okolicy(self, sklep):
        self.sklepy.append(sklep)
		
mieszkanie_1 = Mieszkanie(70, 3, 2, "Poznan", "Grunwald", "Pierwotny", 700000, 500)

mieszkanie_1.dodaj_sklepy_w_okolicy("Biedronka")
mieszkanie_1.dodaj_sklepy_w_okolicy("Lidl")
mieszkanie_1.dodaj_sklepy_w_okolicy("Żabka")
mieszkanie_1.dodaj_sklepy_w_okolicy("Spar")


print(mieszkanie_1)
print("Cena za metr kwadratowy: " + str(mieszkanie_1.oblicz_cene_mkw()) + " zł")
print("Sklepy w okolicy: " + ", ".join(mieszkanie_1.sklepy))