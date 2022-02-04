import math

# operatori de assignare
x = 3 # asignare = stocarea unei valori la o anumita adresa de memorie
print(x)
x = x + 3 # crestem valoarea lui x cu 3
print(x)
x += 3 # face acelasi lucru cu x=x+3
print(x)
x = x - 3
print(x)
x -= 3
print(x)
x = x * 3
print(x)
x *= 3
print(x)
x = x / 3
print(x)
x /= 3
print(x)
print('------------')

# operatori aritmetici
print(10%3) # restul impartirii 10 la 3 = rest 1
print(2**3) # 2 la puterea a 3a
x = 9
print(x**(1/2)) # x la puterea 1/2 sau radical din x

# operatori de comparare
x = 5
y = 3
print(x==y) # operator de comparatie, daca x = y -> rezultat True/False
x = y
print(x == y)
x = 5
print(x!=y) # verifica daca valorile din variabile sunt diferite
print(x<y)
print(x<=y)
print(x>y)
print(x>=y)
print('----------')
# operatori logici
'''
operatorii logici sunt : and, or, not
intotdeauna operatorul and are prioritate in fata operatorului or
'''
print(x<2 and x<y) # ambele conditii trebuie sa fie True pentru a avea toata conditia evaluata ca si True
print(x>2 and x<y)
print(x>2 and x<y or y>2) # 5*3+2
print(x>2 or x<y and y>2)
print(x>2 and (x<y or y>2)) # 5*(3+2)
# 5*3+2
# 5*(3+2)
print('-------')
pasaport = input('Introduceti validarea pasaportul : DA/NU ')
ambii_parinti = input('Are ambii parinti? DA/NU ')
permisiune = input('Are permisiune? DA/NU/NA ')
if pasaport == 'DA' and (ambii_parinti == 'DA' or permisiune == 'DA') :
    print('Permite calatoria')
else :
    print('Nu permite calatoria')

NOTA_DE_TRECERE = 5 # o constanta se scrie cu litere mari si se doreste sa nu se schimbe valoarea
NOTA_DE_TRECERE_PURTARE = 7
nota_examen = int(input('Introdu nota la examen '))
nota_purtare = int(input('Introdu nota la purtare '))
if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE :
    print('Bravo ai trecut!')
    if nota_examen == 10 and nota_purtare == 10 : # acest if se executa doar daca conditia de la linia 68 este evaluata ca si adevarata
        print('Felicitari esti premiat!')
else :
    print('Nu ai trecut clasa!')

# not - da valoarea inversa (daca e true da false si invers)
