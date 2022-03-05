# 1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while

print('--------ex 1-----------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

print('--------FOR in range/simplu--------')
for i in range(len(masini)) :
    print(f'FOR simplu/in range : Masina mea preferata ests {masini[i]}')

print('--------FOR EACH--------')
for masina in masini :
    print(f'FOR EACH: Masina mea preferata este {masina}')

print('--------WHILE--------')
i = 0
while i < len(masini) :
    print(f'WHILE : Masina mea preferata este {masini[i]}')
    i += 1

# 2. Aceeasi lista. Folositi un for else :
# In for - Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else - Printati lista

print('--------ex 2-----------')
# nr = len(masini)
# print(f'Avem {nr} masini')
# for i in range(1, nr-1) :
#     masini[i] = masini[i].upper()
# #print(f'Elementele scrie cu majuscule inafara de primul si ultimul sunt : {masini}')
# else :
#     print(f'Noua lista este {masini}')

#ALTA VARIANTA :
for i in range(len(masini)):
   if not(i==0 or i==len(masini)-1):
      print(masini[i].upper())
   else :
      print(masini[i])

# 3. Aceeasi lista. Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes : Printam ‘am gasit masina dorita de dvs’, Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel Printam Am gasit masina X. Mai cautam

print('--------ex 3-----------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini :
    if masina == 'Mercedes' :
        print(f'Am gasit masina dorita de dvs. {masina}')
        break
    else :
        print(f'Am gasit masina {masina}. Mai cautam')

# 4. Aceasi lista. Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun. Folositi un cuvant cheie care sa dea skip la ce urmeaza (nu trebuie else)
# Printati S-ar putea sa va placa masina x

print('--------ex 4-----------')
for masina in masini :
    if masina != 'Trabant' and masina != 'Lastun':
        print(f'S-ar putea sa va placa masina {masina}')

# ALTA VARIANTA cu un cuvant cheie sa dea skip :
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i]=='Lastun':
      continue
    print(f'S-ar putea sa va placa masina {masini[i]}')

# 5. Modernizati parcul de masini. Creati o lista goala, masini_vechi. Iterati prin masini
# Cand gasiti Lastun sau Trabant:
#     Salvati aceste masini in masini_vechi
#     Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
#     Printati Modele vechi: x
#     Modele noi: x

print('--------ex 5-----------')
masini_vechi = []
for i in range(len(masini)) :
    if masini[i] == 'Trabant' or masini[i] == 'Lastun' :
        masini_vechi.append(masini[i])
        # masini_vechi.insert(0, 'Trabant')
        # masini_vechi.insert(0, 'Lastun')
        masini[i] = 'Tesla'
        # break
print(f'Modele vechi : {masini_vechi}')
print(f'Modele noi : {masini}')

# 6. Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun. Iterati prin lista

print('--------ex 6-----------')
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for masina, pret in pret_masini.items():
   if pret < 15000 :
       print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina} la pretul de {pret}')

# ALTA VARIANTA :
# for masina in pret_masini.keys():
#      if pret_masini[masina] <= 15000 :
#         print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina}')

# 7. Avand lista numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea. Afisati de cate ori apare 3. (nu aveti voie sa folositi count)

print('--------ex 7-----------')
x = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in numere :
    if i == 3 :
        x = x + 1
print(f'Cifra 3 apare de {x} ori')

# 8. Aceeasi lista. Iterati prin ea. Calculati si afisati suma numerelor (nu aveti voie sa folositi sum)

print('--------ex 8-----------')
suma = 0
for i in numere :
    suma = suma + i
print(f'Suma numerelor este {suma}')

# 9. Aceeasi lista. Iterati prin ea. Afisati cel mai mare numar (nu aveti voie sa folositi max)

print('--------ex 9-----------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max_nbr = 0
for maxim in numere :
    if maxim > max_nbr :
        max_nbr = maxim
print(f'Valoarea maxima este {max_nbr}')

# ALTA VARIANTA
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = 0
pozitie = 0
while pozitie < len(numere) :
    if max < numere[pozitie] :
       max = numere[pozitie]
    pozitie += 1
print(f'Valoarea maxima este {max}')

# 10.Aceeasi lista. Iterati prin ea. Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

print('--------ex 10-----------')
# for i in numere :
#     numere = -abs(i)
#     print(f'Numarul pozitiv transformat in negativ este : {numere}') -> nu mai afiseaza o lista, ci fiecare pe alta linie

# ALTA VARIANTA
for i in range(len(numere)) :
    if numere[i] > 0 :
        numere[i] = -numere[i]
print(f'Numerele modificate sunt : {numere}')

print('----------OPTIONALE-----------')
# 11.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere. Populati corect celelalte liste. Afisati cele 4 liste la final

print('--------ex 11 optional-----------')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for nr in alte_numere :
    if nr % 2 == 0 and nr > 0 :
        numere_pare.append(nr)
        numere_pozitive.append(nr)
    elif nr % 2 ==0 and nr < 0:
        numere_pare.append(nr)
        numere_negative.append(nr)
    elif nr % 2 == 1 and nr > 0 :
        numere_impare.append(nr)
        numere_pozitive.append(nr)
    elif nr % 2 == 1 and nr < 0 :
        numere_impare.append(nr)
        numere_negative.append(nr)

#ALTA VARIANTA
# for nr in alte_numere:
#     if nr%2==0:
#         numere_pare.append(nr)
#         if nr < 0:
#             numere_negative.append(nr)
#         else:
#             numere_pozitive.append(nr)
#     else:
#         numere_impare.append(nr)
#         if nr < 0:
#             numere_negative.append(nr)
#         else:
#             numere_pozitive.append(nr)

print(f'Lista cu numere pare este {numere_pare}')
print(f'Lista cu numere impare este {numere_impare}')
print(f'Lista cu numere pozitive este {numere_pozitive}')
print(f'Lista cu numere negative este {numere_negative}')

# 12. Aceeasi lista. Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici : https://www.youtube.com/watch?v=lyZQPjUT5B4

print('--------ex 12 optional-----------')
print(f'Lista originala este {alte_numere}')
for i in range(len(alte_numere)) :
    for j in range(len(alte_numere) - 1 ) : # m-am ajutat de internet, dar nu prea inteleg de ce s-a mai facut si partea asta
        if alte_numere[j] > alte_numere[j+1] :
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
print(f'Lista ordonata este {alte_numere}')

#ALTA VARIANTA
# for j in range(len(alte_numere)) :
#     swap = False
#     i = 0
#     while i<len(alte_numere)-1 :
#         if alte_numere[i] > alte_numere[i+1]
#             alte_numere[i], alte_numere[i+1] = alte_numere[i+1], alte_numere[i]
#               swap = True
#             i = i + 1
#       if swap == False :
#           break
# print(f'Lista sort este {alte_numere}')

# 13. Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

print('--------ex 13 optional-----------')
numar_secret = int(input('Generati un numar random intre 1 si 30 : '))
numar_ghicit = None
while numar_secret >=0 and numar_secret <= 30 :
    numar_ghicit = int(input('Alege un numar : '))
    if numar_secret > numar_ghicit :
        print('Numarul secret este mai mare')
    elif numar_secret < numar_ghicit :
        print('Numarul secret e mai mic')
    else :
        print('Felicitari! Ai ghicit')
    break

#ALTA VARIANTA
# numar_secret = int(input('Generati un numar random intre 1 si 30 : '))
# numar_ghicit = None
# while numar_secret >=0 and numar_secret <= 30 :
#     numar_ghicit = int(input('Alege un numar : '))
#     if numar_secret > numar_ghicit :
#         print('Numarul secret este mai mare')
#     elif numar_secret < numar_ghicit :
#         print('Numarul secret e mai mic')
#     else :
#         print('Felicitari! Ai ghicit')
#     break

# 14. Alegeti un numar de la tastatura. Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333

print('--------ex 14 optional-----------')
numar = int(input('Alegeti un numar : '))
for i in range(1, numar+1) :
    print(f'{i}' * i)

# 15.tastatura_telefon = [
#                           [1, 2, 3],
#                           [4, 5, 6],
#                           [7, 8, 9],
#                           [0]
#                          ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

print('--------ex 15 optional-----------')
tastatura_telefon = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [0]
                    ]
for i in range(len(tastatura_telefon)) :
    for j in range(len(tastatura_telefon[i])) :
        print(f'Cifra curenta este : {tastatura_telefon[i][j]}')

