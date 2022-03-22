from datetime import date

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
print('------------1------------')
class Cerc:
    # atribute raza si culoare
    raza = None
    culoare = None
    # constructor
    def __init__(self, raza, culoare) :
        self.raza = raza
        self.culoare = culoare
    # metode
    def descrie_cerc(self, raza, culoare):
        return f'Raza cercului este {raza} si culoarea {culoare}'
    def aria(self, raza):
        aria = 3.14 * (raza**2)
        return f'Aria cercului este {aria}'
    def diametru(self, raza):
        diametru = 2 * raza
        return f'Diametrul cercului este {diametru}'
    def circumferinta(self, raza):
        circumferinta = 3.14 * (raza * 2)
        return f'Circumferinta cercului este {circumferinta}'

cerc1 = Cerc(2, 'turcoaz')
print(cerc1.descrie_cerc(2, 'turcoaz'))
print(cerc1.aria(2))
print(cerc1.diametru(2))
print(cerc1.circumferinta(2))

cerc2 = Cerc(1, 'fucsia')
print(cerc2.descrie_cerc(1, 'fucsia'))
print(cerc2.aria(1))
print(cerc2.diametru(1))
print(cerc2.circumferinta(1))

# 2 Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

print('------------2------------')
class Dreptunghi:
    # atribute lungime, latime si culoare
    lungime = None
    latime = None
    culoare = None

    # constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    # metode
    def descrie(self, lungime, latime, culoare):
        return f'Dreptunghiul are lungimea {lungime}, latimea {latime} si este de culoarea {culoare}'
    def aria(self, lungime, latime):
        aria = lungime * latime
        return f'Aria dreptunghiului este {aria}'
    def perimetrul(self, lungime, latime):
        perimetrul = 2 * (lungime + latime)
        return f'Perimetrul dreptunghiului este {perimetrul}'
    def schimba_culoare(self, noua_culoare):
        self.noua_culoare = 'turcoaz'

noua_culoare = 'turcoaz'
dreptunghi1 = Dreptunghi(4, 2, 'rosu')
print(dreptunghi1.descrie(4, 2, 'rosu'))
print(dreptunghi1.aria(4, 2))
print(dreptunghi1.perimetrul(4, 2))
dreptunghi1.culoare = noua_culoare
print(dreptunghi1.descrie(4, 2, noua_culoare))

dreptunghi2 = Dreptunghi(6, 3, 'alb')
print(dreptunghi2.descrie(6, 3, 'alb'))
print(dreptunghi2.aria(6, 3))
print(dreptunghi2.perimetrul(6, 3))
dreptunghi2.culoare = noua_culoare
print(dreptunghi2.descrie(6, 3, noua_culoare))

#3.  Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
print('------------3------------')
class Angajat:
    # atribute
    nume = None
    prenume = None
    salariu = None
    # constructor
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    # metode
    def descrie(self, nume, prenume, salariu):
        return f'Angajatul se numeste {nume} {prenume} si are salariul de {salariu} lei'
    def nume_complet(self, nume, prenume):
        return f'Angajatul se numeste {nume} {prenume}'
    def salariu_lunar(self, nume, prenume, salariu):
        return f'Angajatul {nume} {prenume} are salariul lunar de {salariu} lei'
    def salariu_anual(self, nume, prenume, salariu):
        return f'Angajatul {nume} {prenume} are salariul anual de {salariu*12} lei'
    def marire_salariu(self, nume, prenume, procent):
        return f'Angajatul {nume} {prenume} primeste o marire de {procent}%'

angajat1 = Angajat('Crisan', 'Roxana', 600)
print(angajat1.descrie('Crisan', 'Roxana', 600))
print(angajat1.nume_complet('Crisan', 'Roxana'))
print(angajat1.salariu_lunar('Crisan', 'Roxana', 600))
print(angajat1.salariu_anual('Crisan', 'Roxana', 600))
print(angajat1.marire_salariu('Crisan', 'Roxana', 10))

angajat2 = Angajat('Pop', 'Andrei', 100)
print(angajat2.descrie('Pop', 'Andrei', 100))
print(angajat2.nume_complet('Pop', 'Andrei'))
print(angajat2.salariu_lunar('Pop', 'Andrei', 100))
print(angajat2.salariu_anual('Pop', 'Andrei', 100))
print(angajat2.marire_salariu('Pop', 'Andrei', 5))

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

print('------------4------------')
# class Factura:
#     # atribute
#     seria = '123456'
#     numar = None
#     nume_produs = None
#     cantitate = None
#     pret_buc = None
#     # constructor
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#     # metode
#     def schimba_cantitatea(self, cantitate):
#         cantitate_nou = int(input('Introduceti noua cantitate : '))
#         return f'Noua cantitate comandata este de {cantitate_nou} bucati'
#     def schimba_pretul(self, pret):
#         pret_nou = int(input('Introduceti noul pret : '))
#         return f'Noul pret este de {pret_nou} lei'
#     def schimba_nume_produs(self, nume):
#         nume_produs_nou = input('Introduceti noul nume al produsului : ')
#         return f'Noul nume al produsului este {nume_produs_nou}'
#     def genereaza_factura(self, numar, nume_produs, cantitate, pret_buc):
#         # return f'Factura seria {seria} si numarul {numar}'
#         # today = date.today
#         print(f'{date.today} :')
#         return f'{nume_produs} / {cantitate} buc. / {pret_buc} lei / Total : {cantitate * pret_buc} lei'
#         print(f'Telefon |      7       |       700       | 49000')
#
# factura1 = Factura(16655, 'carlig', 5, 5)
# print(factura1.schimba_cantitatea(10))
# print(factura1.schimba_pretul(100))
# print(factura1.schimba_nume_produs('surub'))
# print(factura1.genereaza_factura(155333, 'piulita', 25, 10))

# 5. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

print('------------5------------')
class Cont:
    # atribute
    iban = None
    titular_cont = None
    sold = None
    # constructor
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    # metode
    def afisare_sold(self, iban, titular_cont, sold):
        return f'Titularul {titular_cont} are in contul {iban} suma de {sold} lei'
    def debitare_cont(self, sold, suma):
        sold = sold - suma
        return f'Dupa debitarea sumei de {suma} lei, noul sold este de {sold} lei'
    def creditare_cont(self, sold, suma):
        sold = sold + suma
        return f'Dupa creditarea sumei de {suma} lei, noul sold este de {sold} lei'

titular1 = Cont('RO222INGB3330', 'Crisan Roxana', 1000)
print(titular1.afisare_sold('RO222INGB3330', 'Crisan Roxana', 1000))
print(titular1.debitare_cont(1000, 50))
print(titular1.creditare_cont(1000, 500))

titular2 = Cont('RO111INGB4444', 'Pop Andrei', 350)
print(titular2.afisare_sold('RO111INGB4444', 'Pop Andrei', 350))
print(titular2.debitare_cont(350, 15))
print(titular2.creditare_cont(350, 50))

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
print('------------6 BONUS------------')
class Masina:
    # atribute
    marca = None
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = ('rosu', 'alb', 'verde', 'albastru', 'negru', 'cameleon')
    inmatriculata = False
    # constructor
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    # metode
    def descrie(self, marca, model, viteza_actuala, viteza_maxima, culoare, inmatriculata):
        return f'Masina {marca} {model} are viteza actuala de {viteza_actuala} km/h si viteza maxima de {viteza_maxima} km/h, are culoarea {culoare} si este inmatriculata {inmatriculata}'
    def inmatriculare(self, inmatriculata):
        inmatriculata = True
        return f'Masina este inmatriculata? {inmatriculata}'
    def vopseste(self,culoare, noua_culoare):
        if noua_culoare in culori_disponibile :
            return f'Masina {culoare} este vopsita in {noua_culoare}'
        else :
            return f'Culoarea nu este disponibila, alegeti alta culoare'
    def accelereaza_viteza(self, viteza, viteza_maxima):
        if viteza < 0 :
            return f'Viteza este negativa si nu este buna'
        elif viteza > viteza_maxima :
            return f'Masina a accelerat la {viteza_maxima} km/h'
        else :
            return f'Masina a accelerat la viteza {viteza} km/h'
    def franeaza(self):
        return f'Masina a oprit si are 0 km/h'
masina1 = Masina('Golf', 280)
print(masina1.descrie('VW', 'Golf', 0, 280, 'rosu', False))
print(masina1.inmatriculare(False))
print(masina1.vopseste('gri', 'roz'))