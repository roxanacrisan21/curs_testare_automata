# Liste
nume = 'Mihai'
len(nume)
nume_list = ['M','i','h','a','i'] # aici am definit o lista cu 5 elemente
print(nume_list[0]) # se printeaza primul element din lista
print(len(nume_list)) # afiseaza cate elemente sunt in lista
print(nume_list[0:2]) # slice-ing se poate aplica si pe liste
            # limita superioara a intervalului nu se ia in considerare (adica e pana la 2 dar fara 2)
print(nume_list)
rm = nume_list.remove('a') # scoatem un element din lista (litera 'a')
print(nume_list)

pp = nume_list.pop(2) # scoate ultimul caracter din lista
print(nume_list)

print(f'caracterul scos este : {rm}') # scoate elementul din lista dar nu zice care -> None
print(f'caracterul scos este : {pp}') # ne zice care caracter il scoate -> h
''' diferente intre .pop si .remove : 
- remove sterge 1 singur caracter intre paranteze () iar pop sterge 1 singur caracter in functie de index
- remove nu returneaza nimic, dar pop returneaza o valoare
 pop - Remove and return item at index (default last).
 remove - Remove first occurrence of value  '''

# cum suprascriem valoarea de la o anumita pozitie
nume_list[1] = 'o' # caracterul cu index 1 (caract 2) este schimbat cu 'o'
print(nume_list)

# cum adaugam un element intr-o anumita pozitie
nume_list.insert(2, 'R') # in pozitia 2 (caract 3) este mutat in dreapta si se adauga 'R'
print(nume_list)

nume_list.append('T') # adaugam un element la finalul listei
print(nume_list)

# cum punem o lista intr-o alta lista
lista_in_lista = [
                [1,2,3],
                [4,5,6],
                ['a','b','c']
                ]
print(lista_in_lista) # printam toata lista
print(lista_in_lista[2]) # printam doar lista de la indexul 2 din lista
print(lista_in_lista[2][2]) # printam valoarea cu indexul 2 din lista cu indexul 2
print(lista_in_lista[2][2],lista_in_lista[0][1]) # printam mai multe elemente din liste (cele alese)

# Set

vocale = {'A','E','I','O','U'}
print(type(nume_list)) # printeaza tipul
print(type(vocale))
print(vocale)
# print(vocale[0]) # nu putem printa elementul din pozitia 0; nu se pot printa doar anumite elemente din set
#print(vocale.add('F')) # nu putem adauga
# print(vocale.count('a')) # nu putem numara

litera = input('Introduceti o litera ').upper() #daca introducem litera mica sa o transforme in mare (pt ca asa e in lista)
if litera in vocale :
    print('litera introdusa este o vocala')
else :
    print('litera nu este o vocala')

# Tuple/tuplu - este imutabil (ce este definit nu se mai poate schimba), permite valori si e ordonata
camere_hotel = (1,2,3,4,5,5)
print(camere_hotel[0]) # printare prima camera (index 0)
print(camere_hotel.count(5)) # numara de cate ori este acea cifra in tuplu
# functia count returneaza de cate ori apare elementul in tuplu
print(camere_hotel.index(3)) # index - returneaza pozitia (indexul) in care se afla elementul 3
# functia index returneaza pozitia elementului in tuplu
print(len(camere_hotel)) # afiseaza numarul de elemente din tuplu

# Dict = dictionare = structura care stocheaza informatii in formatul cheie : valoare
capitale = {
    'Romania' : 'Bucuresti', # se pot pune si pe aceeasi linie
    'Italia' : 'Roma',
    'Franta' : 'Paris'
}
print(capitale)
print(capitale['Romania']) # accesare informatiilor din dictionar in functie de cheia 'Romania'
print(capitale.get('Romania')) # la fel dar alt mod de a afisa ce e la cheia 'Romania'

# cum actualizam o informatie
capitale['Romania'] = 'Cluj' # inlocuim informatia de la o anumita cheie
print(capitale['Romania'])

# cum adaugam o informatie
capitale['Rusia'] = 'Moscova' # adaugam in dictionar, se adauga la final pt ca nu putem accesa pozitia elementelor
print(capitale)
print(len(capitale))

# cum putem sterge o informatie existenta
capitale.pop('Italia')
print(capitale)
