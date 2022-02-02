# select apoi ctrl+/ pentru a comenta/decomenta la mai multe linii

import math #importam librarie (cod) externa

print('Hello world!')
print("Hello world!")
print('Mc\'Donalds')  #daca avem ceva de printat cu ' punem \ ca sa nu inchida ce vrem sa scriem
print("Mc'Donalds")
print('Mc"Donalds')

#am declarat si initializat variabile
marca_masina = 'Volvo' #snake case - se prefera mai mult in python
modelMasina = 'XC60' #camel case

#suprascriem
modelMasina = 'V60'

#putem schimba tipul de date
modelMasina = 60

#one line initialization
x, y, z = 'Banana', 'Mar', 'Portocala'
print(z)
print(x, y, z)
a = b = c = 33
print (a, b ,c)

marca = 'Dacia' #string - sir de caractere (se poate litere, cifre sau alte caractere)
an_fabricatie = 1987 #int - nr intreg
pret = 2300.500 #float - nr zecial
inmatriculat = False #boole - A/F

a = 3.64567
print('{:.2f}'.format(a)) #limiteaza nr de zeciale la 2
print(round(a)) #rontunjim
print(math.floor(a)) #fortam rotunjirea in jos
print(math.ceil(a)) #fortam rotunjirea in sus

# #cum aflam tipuri de date
# a = 3
# print(type(3)) #tipul de date

#type casting = schimbare a tipului de date
cifra = '3'
cifra2 = int(cifra) #schimbam tipul din string in int
print(type(cifra))
print(type(cifra2))

nume = 'Crisan'
prenume = 'Roxana'
varsta = 34
print('Numele meu complet este '+ nume + ' '+ prenume)
print('Ma numesc ' + prenume + ' si am varsta de ' + str(varsta)) #varianta 1
#f vine de la format string, si forteaza toate variabilele sa fie stringuri
print(f'Ma numesc {prenume} si am varsta de {varsta}') #varianta 2 - aceasta varianta este recomandata
print("numele meu este {1} {0}".format(nume,prenume)) #varianta 3

#assert = verificare daca ecuatia este true
#daca e True, mergem mai departe silently (nu se intampla nimic)
#daca e False, cod rosu de eroare si nu mergem mai departe
a = 1
#il intreb pe python daca a este egal cu 1
print (a == 1)
assert a == 1  #conditia e true si se trece mai departe
print('trec pe aici')
# assert a == 2  #conditia e false si se opreste/da eroare
# print ('nu mai ajung aici')

# user_pass = input('introdu parola ')
# parola = 'pass123'
# assert parola == user_pass
# print('autentificare reusita')

# #input
# a = 3
# b = int(input('alege un nr ')) #forteaza ca nr introdus sa fie int pt ca by deafult e string, altfel da eroare
# print(a + b)
#
# #pt input mai multe deodata
# name, age, gender = input('Enter Name|Age|Gender (separated by | sign):').split('|')
# print(name)
# print(age)
# print(gender)
# # default la split e sa delimiteze dupa spatiu

#functii string - metode
nume = 'roxi'
print(nume.count('r'))
print(nume.upper())
print(nume.replace('i', 'y'))

#string index
print(nume[2]) # numaratoarea incepe de la 0

#string slicing
#https://stackoverflow.com/questions/509211/understanding-slice-notation
#my_string[de unde incepem : pana unde mergem : din cat in cat]
#pasul e optional - din cat in cat

myStr = 'Azi e miercuri'
# vreau sa il parcurg pana la penultimul
# aflu ultimult index
last_index = len(myStr)-1 #-1 pt ca numaratoarea incepe de la 0
#verificare
print(last_index)
print(myStr[last_index])
print(myStr[13])
#parcurgerea
print(myStr[0:last_index]) #pana la penultimul
print(myStr[0:last_index-1:2]) #pana la ante-penultimul din 2 in 2

#parcurgere inversa
print(myStr[::-1]) # coada : inceput : -1
