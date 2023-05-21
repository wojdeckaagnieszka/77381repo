# zadanie 1.1

hello = "Hello"
student = "Ola"
print("{} {}" .format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie ")
print("Hello " + student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: {}".format(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for x in studenci:
    print("Hello " + x)

# zadanie 1.5

liczba = 3
potega = 4
wynik = liczba**potega
print("Wynik wynosi: {}" .format(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
sort = sorted(studenci)
print("Alfabetyczna lista studentow wynosi: ")
for student in sort:
    print(student)

# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
posortowani = sorted(studenci, key=lambda student: student.split(" ")[1])
print("Alfabetyczna lista studentow wynosi: ")
for student in posortowani:
    print(student)

# zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
licznik = 0
for student in studenci:
    imie, nazwisko = student.split(" ")
    if nazwisko.startswith("N"):
        licznik += 1
liczba_n = licznik
print("Liczba studentow na N wynosi: {}" .format(liczba_n))

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def czy_jest_funkcja_liniowa(punkty: list):
    # Prosta AB
    wspolczynnik_a_AB= (punkty[1][1] -  punkty[0][1]) / (punkty[1][0] -  punkty[0][0])

    #prosta AC
    wspolczynnik_a_AC = (punkty[2][1] -  punkty[0][1]) / (punkty[2][0] -  punkty[0][0])

    if wspolczynnik_a_AB == wspolczynnik_a_AC:
        return True
    else:
        return False

wynik_1 = czy_jest_funkcja_liniowa(wykres_1)
wynik_2 = czy_jest_funkcja_liniowa(wykres_2)
wynik_3 = czy_jest_funkcja_liniowa(wykres_3)

print(wynik_1, wynik_2, wynik_3)