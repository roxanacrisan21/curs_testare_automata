# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# Afiseaz-o
# Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# Printeaza varianta actuala (inversata)
# Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
# (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi
# intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
# Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Notele muzicale sunt : {note_muzicale}')
note_muzicale = note_muzicale[::-1] # am suprascris lista cu elementele inversate, de la coada la cap
print(f'Noua lista de note muzicale inversate este : {note_muzicale}')
note_muzicale.reverse() # functie ce inverseaza ordinea elementelor din lista - se inverseaza din nou
print(f'Lista reinversata cu functia automata : {note_muzicale}') # se ajunge din nou la lista actuala

# 2. De cate ori apare ‘do’?

print(note_muzicale.count('do'))

# 3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
# Afisati lista ordonata astfel [0,1,2,3,4,5,6]

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
total1 = lista1 + lista2
print(f'Varianta 1 cu listele unite : {total1}')
lista1.extend(lista2)
print(f'Varianta 2 cu listele unite : {lista1}')
total1.sort() # sorteaza lista
print(f'Lista ordonata cu varianta 1 este : {total1}')

# 4. Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
lista1.sort()
print(f'Lista ordonata este : {lista1}')
lista1.remove(0)
# lista1.pop(0) # alta metoda
print(f'Lista fara 0 este : {lista1}')

# 5. Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala
print(f'Lista de la exercitiul 3 este : {total1}')
if total1 == [] :
    print('Lista este goala')
else :
    print('Lista nu este goala')

# 6. Folositi o functie care sa stearga lista de la ex3
total1.clear()
print(f'Lista stearsa este : {total1}')

# 7. Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala

# optiunea 1
if total1 == [] :
    print('Lista este goala')
else :
    print('Lista nu este goala')

# optiunea 2
# if len(total1) == 0 :
#     print('Lista este goala')
# else :
#     print('Lista nu este goala')

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(f'Elevii sunt : {dict1.keys()}')

# 9. Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

# 10. Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare
dict1['Dorel'] = '6'
print(f"Dorel a luat nota {dict1['Dorel']} dupa contestatie")

# 11. Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi
dict1.pop('Dorel')
print(f'Noul dictionar al elevilor dupa plecarea lui Dorel este : {dict1}')
dict1['Ionica'] = 9
print(f'Noul dictionar al elevilor dupa venirea lui Ionica este : {dict1}')

# 12. Set :
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni') #exista deja in lista deci nu il mai adauga, set-urile au valori unice
print(zile_sapt)
zile_sapt.add('alta_zi')
print(zile_sapt) # aceasta zi nu exista in set deci se poate adauga

# 13. Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt) :
    print('Weekend este un subset al zilelor din sapt')
else :
    print('Weekend nu este un subset al zilelor din sapt')

# 14. Afisati diferentele dintre aceste 2 seturi
print(zile_sapt.difference(weekend)) # ce e diferit in zile_sapt fata de weekend
print(weekend.difference(zile_sapt)) # ce e diferit in weekend fata de zile_sapt -> adica nimic

# 15. Afisati intersectia elementelor din aceste 2 seturi
print(f'Intersectia celor 2 seturi este : {zile_sapt.intersection(weekend)}')

print('OPTINAL : ')
# 16. Optional
# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
# Testati codul cu diferite valori
jucatori = ['Andrei', 'Razvan', 'Florin', 'Mihai', 'Alexandru'] # Declara o Lista cu 5 jucatori
rezerva = ['Alin', 'Iulian' , 'Cristi'] # Declara o lista cu jucatori de rezerva
schimbari_efectuate = 0 # Schimbari_efectuate = va jucati voi cu valori diferite
if 'Mihai' in jucatori and schimbari_efectuate <= 3 : # Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
    jucatori.remove('Mihai') # Stergem jucatorul scos din lista
    jucatori.insert(0, 'Alin') # Adaugam jucatorul intrat
    rezerva.remove('Alin') # Stergem jucatorul intrat din lista de rezerva
    rezerva.insert(0, 'Mihai') # Adaugam jucatorul iesit la lista de rezerva
    schimbari_efectuate = schimbari_efectuate + 1 # incrementare nr schimbari
    print(f'A iesit Mihai, a intrat Alin, mai avem {3 - schimbari_efectuate} schimbari')
    print(f'Acum jucatorii sunt : {jucatori}')
    print(f'Acum lista de rezerva este : {rezerva}')
else : # Daca jucatorul nu e in teren:
    print('Nu se poate efectua schimbare deoarece jucatorul nu este in teren')
print(f'Mai avem {3 - schimbari_efectuate} schimbari') # cate schimbari mai avem din maxim 3

# alta varianta
# SCHIMBARI_MAXIME = 3
# schimbari_efectuate = 0
# schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
# echipa = {'j1','j2','j3','j4','j5'}
# jucator_in = 'j6'
# jucator_out = 'j1'
# if jucator_out in echipa and schimbari_efectuate <SCHIMBARI_MAXIME:
#     if jucator_in in echipa:
#         print("Nu putem face schimbarea deoarece jucatorul introdus este deja in teren")
#     else:
#         echipa.remove(jucator_out)
#         echipa.add(jucator_in)
#         schimbari_ramase -= 1
#         print(f"A intrat {jucator_in} si a iesit {jucator_out}. Mai aveti {schimbari_ramase} schimbari disponibile")
#         print(f"Actuala echipa este {echipa}")
# else:
#     if schimbari_ramase<=0:
#         print("Nu mai ai schimbari disponibile")
#     print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_in} nu este in teren")