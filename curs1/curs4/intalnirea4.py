# While / while else

print('------------while-----------')
i = 0
while i <= 3 :
    print(f'Valoarea curenta a contorului este {i}')
    i += 1
    # i = i + 1
    print(f'Valoarea contorului dupa incrementare este {i}')
else :
    print('Task completed') # se va executa actiunea o singura data, dupa ce conditia de evaluare nu mai este indeplinita


print('------------for-----------')
for i in range(40) :
    print(i) # se printeaza de la 0 la 39, adica 40 de numere

for i in range(1, 102) :
    print(f'Acesta e dalmatianul cu numarul {i}') # pentru a printa de la 1 nu de la 0

for i in range(0, 101, 2) :
    print(f'Urmatorul numar par este {i}') # pentru a printa nr pare, cu pas de 2

#varianta 1 parcurgere inversa
for i in reversed(range(0, 101, 2)) :
    print(f'Urmatorul numar par este {i}') # pentru a printa nr pare, cu pas de 2, in mod invers

#varianta 2 parcurgere inersa
for i in range(100, 0, -2) :
    print(f'Urmatorul numar par este {i}')

culori = ['albastru', 'alb', 'verde', 'alb', 'rosu']
for culoare in culori :
    print(f'Culoarea curenta este {culoare}') # se parcuge toata lista pe rand

for i in range(len(culori)) :
    if culori[i] == 'alb' :
        culori[i] = 'mov'
        print(f'Lista curenta este {culori} ')
print(f'Lista finala este {culori}')

for culoare in culori :
    if culoare == 'mov' :
        index = culori.index('mov')
        culori[index] = 'magenta'
        print(f'Culoarea curenta este {culori[index]}')
print(f'Noua lista este {culori}')

# print('------------break-----------')
# for i in range(len(culori)) :
#     if culori[i] == 'magenta' :
#         culori[i] = 'purpuriu'
#         print(f'Lista curenta este {culori} ')
#         break # se opreste dupa ce gaseste prima culoare magenta in lista, nu mai continua sa mai caute
# print(f'Lista finala este {culori}')

print('------------continue-----------')
print(culori)
for i in range(len(culori)) :
    if culori[i] == 'magenta' :
        continue
        culori[i] = 'purpuriu'
        print(f'Lista curenta este {culori} ')
print(f'Lista finala este {culori}')

note = [10, 4, 6, 8, 6, 3]
note_premiante = []
for nota in note :
    if nota <= 4 :
        print(f'Studentul curent a picat si a luat nota {nota}') # arata doar cei ce au picat
        continue # sare peste cei picati si ii afiseaza doar pe cei ce au trecut
    note_premiante.append(nota)
print(f'Lista note premiante este {note_premiante}')