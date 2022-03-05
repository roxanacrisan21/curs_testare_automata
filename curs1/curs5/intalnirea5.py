alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for nr in alte_numere:
    if nr%2==0:
        numere_pare.append(nr)
        if nr < 0:
            numere_negative.append(nr)
        else:
            numere_pozitive.append(nr)
    else:
        numere_impare.append(nr)
        if nr < 0:
            numere_negative.append(nr)
        else:
            numere_pozitive.append(nr)
print(f'Lista cu numere pare este {numere_pare}')
print(f'Lista cu numere impare este {numere_impare}')
print(f'Lista cu numere pozitive este {numere_pozitive}')
print(f'Lista cu numere negative este {numere_negative}')