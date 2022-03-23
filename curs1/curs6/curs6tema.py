from datetime import date
from tabulate import tabulate # functia tabulate pentru printrarea tabilara

# explicati urmatoarele chestii:
# Ce este un for, cand se foloseste si cum se foloseste
# Ce este un for each, cand se foloseste si cum se foloseste
# Care e diferenta intre for si foreach
# Ce este un while, cand se foloseste si cum se foloseste.

# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

#1. Clasa Cerc.
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
# print('------------1------------')
# class Cerc:
#     # atribute raza si culoare
#     raza = 0
#     culoare = None
#     # constructor
#     def __init__(self, raza_cerc, culoare_cerc) : # punem constructor ca sa putem sa modificam valorile mai tarziu
#         self.raza = raza_cerc
#         self.culoare = culoare_cerc
#     # metode
#     def descrie_cerc(self):
#         print(f'Raza cercului este {self.raza} si culoarea {self.culoare}') # punem self.raza pentru a lua raza initiata in obiect
#     def aria(self):
#         aria = 3.14 * (self.raza**2)
#         return f'Aria cercului este {aria}'
#     def diametru(self):
#         diametru = 2 * self.raza
#         return f'Diametrul cercului este {diametru}'
#     def circumferinta(self):
#         circumferinta = 3.14 * (self.raza * 2)
#         return f'Circumferinta cercului este {circumferinta}'
#
# cerc1 = Cerc(2, 'turcoaz') #cerc1 este numele obiectului instantiat in clasa Cerc, cu raza 2 si culoarea turcoaz
# cerc1.descrie_cerc() # nu pun cu print pentru ca in functie am pus print. daca puneam return, aici puneam print
# print(cerc1.aria())
# # sau aria = cerc1.aria() si apoi print(aria)
# print(cerc1.diametru())
# print(cerc1.circumferinta())
#
# cerc2 = Cerc(1, 'fucsia')
# print(cerc2.descrie_cerc())
# print(cerc2.aria())
# print(cerc2.diametru())
# print(cerc2.circumferinta())

# 2 Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
#
# print('------------2------------')
# class Dreptunghi:
#     # atribute lungime, latime si culoare
#     lungime = None
#     latime = None
#     culoare = None
#
#     # constructor
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#     # metode
#     def descrie(self, lungime, latime, culoare):
#         return f'Dreptunghiul are lungimea {lungime}, latimea {latime} si este de culoarea {culoare}'
#     def aria(self, lungime, latime):
#         aria = lungime * latime
#         return f'Aria dreptunghiului este {aria}'
#     def perimetrul(self, lungime, latime):
#         perimetrul = 2 * (lungime + latime)
#         return f'Perimetrul dreptunghiului este {perimetrul}'
#     def schimba_culoare(self, noua_culoare):
#         self.noua_culoare = 'turcoaz'
#
# noua_culoare = 'turcoaz'
# dreptunghi1 = Dreptunghi(4, 2, 'rosu')
# print(dreptunghi1.descrie(4, 2, 'rosu'))
# print(dreptunghi1.aria(4, 2))
# print(dreptunghi1.perimetrul(4, 2))
# dreptunghi1.culoare = noua_culoare
# print(dreptunghi1.descrie(4, 2, noua_culoare))
#
# dreptunghi2 = Dreptunghi(6, 3, 'alb')
# print(dreptunghi2.descrie(6, 3, 'alb'))
# print(dreptunghi2.aria(6, 3))
# print(dreptunghi2.perimetrul(6, 3))
# dreptunghi2.culoare = noua_culoare
# print(dreptunghi2.descrie(6, 3, noua_culoare))

#3.  Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
# print('------------3------------')
# class Angajat:
#     # atribute
#     nume = None
#     prenume = None
#     salariu = None
#     # constructor
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#     # metode
#     def descrie(self, nume, prenume, salariu):
#         return f'Angajatul se numeste {nume} {prenume} si are salariul de {salariu} lei'
#     def nume_complet(self, nume, prenume):
#         return f'Angajatul se numeste {nume} {prenume}'
#     def salariu_lunar(self, nume, prenume, salariu):
#         return f'Angajatul {nume} {prenume} are salariul lunar de {salariu} lei'
#     def salariu_anual(self, nume, prenume, salariu):
#         return f'Angajatul {nume} {prenume} are salariul anual de {salariu*12} lei'
#     def marire_salariu(self, nume, prenume, procent):
#         return f'Angajatul {nume} {prenume} primeste o marire de {procent}%'
#
# angajat1 = Angajat('Crisan', 'Roxana', 600)
# print(angajat1.descrie('Crisan', 'Roxana', 600))
# print(angajat1.nume_complet('Crisan', 'Roxana'))
# print(angajat1.salariu_lunar('Crisan', 'Roxana', 600))
# print(angajat1.salariu_anual('Crisan', 'Roxana', 600))
# print(angajat1.marire_salariu('Crisan', 'Roxana', 10))
#
# angajat2 = Angajat('Pop', 'Andrei', 100)
# print(angajat2.descrie('Pop', 'Andrei', 100))
# print(angajat2.nume_complet('Pop', 'Andrei'))
# print(angajat2.salariu_lunar('Pop', 'Andrei', 100))
# print(angajat2.salariu_anual('Pop', 'Andrei', 100))
# print(angajat2.marire_salariu('Pop', 'Andrei', 5))

# 4. Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
#
# print('------------4------------')
# class Factura:
#     # atribute
#     seria = '123456'
#     numar = 0
#     nume_produs = None
#     cantitate = 0
#     pret_buc = 0
#     # constructor
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#     # metode
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate  # modificam cantitatea initiala
#         return self.cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#         return self.pret_buc
#
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#         return self.nume_produs
#
#     def genereaza_factura(self):
#         total = self.pret_buc * self.cantitate
#         print(f' Am generat factura la {self.nume_produs} in cantitate de {self.cantitate} la un pret unitar de {self.pret_buc} avand un total de {total}')
#
# factura1 = Factura(1, 'Factura Gaz', 6, 300)
# factura1.schimba_pretul(460)
# cantitate_finala = factura1.schimba_cantitatea(2) # schimbam cantiatea din 6 in 2
# factura1.genereaza_factura()
# print(cantitate_finala)
# print(factura1.cantitate)

# 5. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
#
# print('------------5------------')
# class Cont:
#     # atribute/fields
#     iban = 0 # daca e int e mai bine sa punem cu 0 nu cu None
#     titular_cont = None # None pentru ca e un string
#     sold = 0
#     # constructor
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#     # metode
#     def afisare_sold(self, iban, titular_cont, sold):
#         return f'Titularul {titular_cont} are in contul {iban} suma de {sold} lei'
#     def debitare_cont(self, suma_debitare):
#         self.sold = self.sold - suma_debitare
#         return f'Noul sold este de {self.sold} lei'
#     def creditare_cont(self, suma_creditare):
#         self.sold = self.sold + suma_creditare
#         return f'Noul sold este de {self.sold} lei'
#
# titular1 = Cont('RO222INGB3330', 'Crisan Roxana', 1000)
# print(titular1.afisare_sold('RO222INGB3330', 'Crisan Roxana', 1000))
# print(titular1.debitare_cont(50))
# print(titular1.creditare_cont(500))

# titular2 = Cont('RO111INGB4444', 'Pop Andrei', 350)
# print(titular2.afisare_sold('RO111INGB4444', 'Pop Andrei', 350))
# print(titular2.debitare_cont(350, 15))
# print(titular2.creditare_cont(350, 50))

# 6. Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0
print('------------6 OPTIONAL------------')
class Masina:
    # atribute
    marca = None
    modelul = None
    viteza_max = 0
    viteza_actuala = 50
    culoare = 'gri'
    culori_disponibile = ('rosu', 'galben', 'verde', 'fuchia', 'magenta', 'ciclam')
    inmatriculata = False
    # constructor
    def __init__(self, marca, model, viteza_maxima):
        self.marca = marca
        self.modelul = model
        self.viteza_max = viteza_maxima
    # metode
    def descrie(self):
        print(f'Masina {self.marca} {self.modelul} are viteza actuala de {self.viteza_actuala} km/h si viteza maxima de {self.viteza_max} km/h, are culoarea {self.culoare} si este inmatriculata {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        return f'Masina este inmatriculata? {self.inmatriculata}'

    def vopseste(self, noua_culoare):
        if noua_culoare in self.culori_disponibile :
            self.culoare = noua_culoare
            return f'Masina este vopsita in {self.culoare}'
        else :
            print (f'Culoarea nu este disponibila, alegeti alta culoare')
            return f'Culoarea a ramas in {self.culoare}'

    def accelereaza_viteza(self, noua_viteza):
        if noua_viteza < 0 :
            print(f'Viteza este negativa si nu este buna')
        elif noua_viteza > self.viteza_max :
            self.viteza_actuala = self.viteza_max
            return f'Masina a accelerat la viteza maxima de {self.viteza_actuala} km/h'
        else :
            self.viteza_actuala = noua_viteza
            return f'Masina a accelerat la viteza {self.viteza_actuala} km/h'

    def franeaza(self, incetinire):
        while self.viteza_actuala > 0:
            self.viteza_actuala = self.viteza_actuala - incetinire
            print(self.viteza_actuala)
        if self.viteza_actuala <= 0 :
            print('Am oprit masina!')
        return f'Masina a incetinit si are {self.viteza_actuala} km/h'

masina1 = Masina('VW', 'Golf', 280)
masina1.descrie()
print(masina1.inmatriculare())
print(masina1.vopseste('verde'))
print(masina1.accelereaza_viteza(160))
print(masina1.franeaza(20))