#1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# O variabila este un spatiu din memorie, cu nume unic, care stocheaza diferite valori, valori care pot fi schimbate
# pe parcursul programului.

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte

import math #importam librarie (cod) externa

var_str = 'Roxana'
var_intreg = 21
var_zecimal = 21.99
var_bol = True

#3. Utilizat functia type pentru a verifica daca au tipul de date asteptat

print(type(var_str))
print(type(var_intreg))
print(type(var_zecimal))
print(type(var_bol))

#4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
#Verificati tipul acesteia

var_zecimal = round(var_zecimal)
print(f'Variabila float rotunjita este {var_zecimal}')

# 5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)

print(f'Variabila de tip string este {var_str} si este de fapt numele meu')
print(f'Variabila de tip int este {var_intreg} si este o zi importanta pentru mine')
print(f'Variabila de tip float este {var_zecimal} si este o deriva de la acea zi')
print(f'Variabila de tip boolean este {var_bol} si este interesanta :)')

# 6. citeste de la tastatura numele; citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

nume = input('Introduceti numele ')
prenume = input('Introduceti prenumele ')

complet = nume + prenume
print(f'Numele complet este {complet}')
nr_char = len(nume+prenume)
print (f'Numele complet are {nr_char} caractere')

# 7. citeste de la tastatura lungimea ; citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'

a = int(input('Introduceti lungimea = '))
b = int(input('Introduceti latimea = '))
aria = a * b
print(f'Aria dreptunghiului este {aria}')

# 8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

my_str = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Scrie un numar = '))
last_index = len(my_str)
print(my_str[0:last_index-x]) #pana la ultimul-x

# 9. acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5

my_str1 = my_str[0:5]
print(my_str1)  #verificare primele 5 caractere
my_str2 = my_str[last_index-5:last_index]
print(my_str2) #verificare ultimele 5 caractere
new_str = my_str1 + my_str2
print(f'Noul string format din primele 5 caractere si ultimele 5 este : {new_str}')

# 10. acelasi string
# afisati de cate ori apare cuvantul 'the'

nr_the = my_str.count('the')
print(f'Cuvantul "the" apare de {nr_the} ori')

# 11. acelasi string
# inlocuieste the cu THE peste tot; printeaza rezultatul

new_change = my_str.replace('the' , 'THE')
print(f'Noul string cu THE mare este : {new_change}')

# 12. acelasi string 'Coral is either the stupidest animal or the smartest rock'
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '

indexx = my_str.find('rock')
print(f'indexul de la rock este : {indexx}')
neww = my_str[0:indexx]
print(f' Stringul pana la index este : {neww}')

# 13. citeste de la tastatura un string
# verifica daca primul si ultimul caracter sunt la fel ;
# se va folosi un assert ; atentie: se doreste ca programul sa fie case insensitive ; 'apA' e acceptat

alt_str = str(input('Scrie un string : '))
p = alt_str[0:1].lower()
print(f'Primul caracter este : {p}')
ultim_index = len(alt_str) #ultimul index
u = alt_str[ultim_index-1:ultim_index].lower()
print(f'Ultimul caracter este : {u}')

assert p == u #verificare daca primul si ultimul caracter sunt la fel
print('corect')
# 14. avand stringul '0123456789', afisati doar numerele pare + acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)

nou_str = '0123456789'
par = nou_str[0::2] #de la 0 se merge din 2 in 2
print(f'Numerele pare din string sunt : {par}')
impar = nou_str[1::2] #de la 1 se merge din 2 in 2
print(f'Numerele impare din string sunt : {impar}')

# 15. acelasi string de la ex 14
# folositi un assert ca sa verificati daca acest string contine doar numere
# indiciu: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
# poate gasim o functie ajutatoare
# Ex: ‘abc123’ => false; ‘abc’ => false, ‘123’ => true

#sa folosesc si un assert?

print(f'Sirul contine doar cifre? {nou_str.isdigit()}')

# 16. citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc

str_impar = input('Scrie un string de dimensiune impara : ')
y = math.floor(len(str_impar)/2)
caract = str_impar[y]
print(f'Caracterul din mijlocul stringului este : {caract}')

# 17. Folosind assert, verificati daca un string este palindrom

# 18.folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare

# 19. citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla

# 20. citeste un user de la tastatura + citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****
