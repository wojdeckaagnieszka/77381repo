def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod

print(f'Pole i obwód wynoszą: {trojkat(10, 15, 12, 0)}')
