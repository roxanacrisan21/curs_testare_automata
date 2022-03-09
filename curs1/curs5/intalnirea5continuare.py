# Functii simple
#
# def say_hi():
#     print('hi')
# say_hi()
#
# # Functii cu parametrii
# def say_hi_v1(user, varsta, ocupatie):  # aici se defineste argumentul/argumentele
#     print(f'Buna {user}, ai  {varsta} ani si esti {ocupatie}')

# nume = input('Introdu userul : ')
# ani = input('Introdu varsta : ')
# ocupatie = input('Introdu ocupatia : ')

#say_hi_v1(nume, ani, ocupatie) # se apeleaza functia cu toti parametrii pusi mai sus
# say_hi()
#
# def say_hi_v2(user):
#     print(f'hi {user}')
# nume_input = ['alex', 'roxy', 'norbi'] # citire dintr-o baza de date
# for nume in nume_input :
#     say_hi_v2(nume)
#
# def calculeaza_impozit(valoare_salariu):
#     if valoare_salariu < 4000 :
#         tax = 0
#     elif valoare_salariu >= 4000 and valoare_salariu < 5000 :
#         tax = 0.10
#     elif valoare_salariu >= 5000 and valoare_salariu < 33500 :
#         tax = 0.22
#     else :
#         tax = 0.4
#     salariu_impozat = valoare_salariu - valoare_salariu*tax
#     impozit = valoare_salariu * tax
#     return f'taxa aplicata a fost de {tax}, iar salariul dupa impozit este {salariu_impozat}. Impozitul este de {impozit}' # ca sa ne dea valoarea inafara functiei calculeaza_impozit
# valoare_salariu = int(input('Introduceti salarul : '))
# taxa = calculeaza_impozit(valoare_salariu)
# print(calculeaza_impozit(valoare_salariu))

#Alta varianta
# def calculeaza_impozit(valoare_salariu):
#     if valoare_salariu < 4000 :
#         tax = 0
#     elif valoare_salariu >= 4000 and valoare_salariu < 5000 :
#         tax = 0.10
#     elif valoare_salariu >= 5000 and valoare_salariu < 33500 :
#         tax = 0.22
#     else :
#         tax = 0.4
#     return tax # ca sa ne dea valoarea inafara functiei calculeaza_impozit
# valoare_salariu = int(input('Introduceti salarul : '))
# taxa = calculeaza_impozit(valoare_salariu)
# salariu_impozat = valoare_salariu - valoare_salariu * taxa
# impozit = valoare_salariu * taxa
# print(f'taxa aplicata a fost de {taxa}, iar salariul dupa impozit este {salariu_impozat}. Impozitul este de {impozit}')

# exercitiu : copii bilet avion < 10 ani = 0; 10-18 ani = -50%, 18-60 = 100%, >65ani = 0
def calcul_pret_bilet(varsta, pret_bilet) :
    while varsta < 0 :
        varsta = int(input('Varsta incorecta. incercati din nou'))
    if varsta < 10 or varsta > 65 :
        pret_bilet = 0
        print('pret 0')
    elif varsta >= 10 and varsta < 18 :
        pret_bilet = pret_bilet - pret_bilet * 0.5
        print('pret 1')
    elif varsta >= 18 and varsta <= 65 :
        pret_bilet = pret_bilet
        print('pret 2')
    return f'aveti varsta de {varsta}. pretul biletului este de {pret_bilet} lei'

if __name__ == 'main': # pentru a nu rula daca functia e apelata in alt fisier (doar in acest fisier)
    varsta = -1
    pret_bilet = 100
    pret_final = calcul_pret_bilet(varsta, pret_bilet)
    print(pret_final)

