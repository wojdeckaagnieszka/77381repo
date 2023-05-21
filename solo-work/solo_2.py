def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod

print(f'Pole i obwód wynoszą: {trojkat(10, 15, 12, 0)}')

def kolo(promien):
    pole = 3.14 * (promien ** 2)
    obwod = 2 * 3.14 * promien
    return pole, obwod
    
print(f'Pole i obwód wynoszą: {kolo(10)}')

def trapezprostokatny(podstawaA, podstawaB, bok, wysokosc):
    pole = (podstawaA + podstawaB) * wysokosc / 2 
    obwod = podstawaA + podstawaB + bok + wysokosc
    return pole, obwod

print(f'Pole i obwód wynoszą: {trapezprostokatny(10, 5, 7, 3)}')

