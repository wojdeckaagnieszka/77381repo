import csv
import os
import random

filename = "solo-work/data/"
os.makedirs(os.path.dirname(filename), exist_ok=True)

with open('solo-work/data/pracownicy.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Katarzyna", "Arbuz", random.randint(1000, 10000)])
    writer.writerow(["Anna", "Pistacja", random.randint(1000, 10000)])
    writer.writerow(["Jacek", "Placek", random.randint(1000, 10000)])