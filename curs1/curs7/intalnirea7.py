# OOP piloni

from abc import ABC, abstractmethod


class Angajat(ABC): # clasa abstracta pt ca are ABC
    @abstractmethod # metoda abstracta
    def pontaj(self):
        raise NotImplementedError # sa dea eroare daca nu avem acea metoda implementata in clasa de mai jos/clasa copil
        # pass
    @abstractmethod
    def testAlcool(self):
        raise NotImplementedError

class AngajatSRI(Angajat):
    __numeProiectAlpha = 'Cod Secret Vulturul'
    nume_vechu = []

    def __init__(selfself, nume_proiect):
        __numeProiectAlpha = nume_proiect

    def pontaj(self):
        frecventaPontareLuna = 1
        return frecventaPontareLuna

    def testAlcool(self):
        frecventaTestAlcool = 8
        return frecventaTestAlcool

    def ascultaTelefoane(self): # se poate implementa chiar daca nu a fost definita in clasa parinte, specifica doar in clasa copil
        tipTelefoaneDeAscultat = 'Smartphone'
        return tipTelefoaneDeAscultat

    @property # ca sa putem accesa variabila privata
    def numeProiectAlpha(self): # se poate pune si alt nume la def
        return self.__numeProiectAlpha
        #pass @ daca nu scriem nimic la acea functie

    @numeProiectAlpha.getter
    def numeProiectAlpha(self):
        print(f'Numele proiectului este {self.__numeProiectAlpha}')
        print(f'Shhh, nu mai spune la nimeni')
        return self.__numeProiectAlpha

    @numeProiectAlpha.setter
    def numeProiectAlpha(self, nume_nou):
        try :
            if (nume_nou not in ('asculta', 'citeste', 'colecteaza')):
                self.nume_vechi.append(self.__numeProiectAlpha)
                self.__numeProiectAlpha = nume_nou
                print(self.__numeProiectAlpha)
            else:
                #print('numele nu este sigur')
                raise NameError('Numele nu este sigur')
        except :
            print('Numele proiectului trebuie definit corect')

    @numeProiectAlpha.deleter
    def numeProiectAlpha(self):
        self.__numeProiectAlpha = None

    # def adauga_nume(self,nume_vechi):
    #     nume_vechi.append(self.__numeProiectAlpha)
    #     print(nume_vechi)

angajatSRI1 = AngajatSRI('Codul Alpha')
angajatSRI1.pontaj()
print(angajatSRI1.ascultaTelefoane())
angajatSRI1.numeProiectAlpha
angajatSRI1.numeProiectAlpha='Codul secret intre Alex si David'
angajatSRI1.numeProiectAlpha
del angajatSRI1.numeProiectAlpha #am sters numele proiectului
angajatSRI1.numeProiectAlpha
angajatSRI1.numeProiectAlpha = "Cod Secret"
angajatSRI1.numeProiectAlpha = "Cod Si mai Secret"
print(angajatSRI1.nume_vechi)

# Suma de *args - adica mai multe numere nedefinite
# def addnr1(x,y,*args):
#     print(x,y,*args)
#     return sum(args)
#
# suma = addnr1(1,2,3,4)
# print(suma)


# super class - Variabile protected
# class Student:
#     # protected data members
#     _name = None
#
#     # constructor
#     def __init__(self, name):
#         self._name = name
#
#
# # derived class
# class  ChildStudent(Student):
#     _classAttribute = "test"
#     # constructor
#     def __init__(self, name):
#         Student.__init__(self, name)
#
#     # public member function
#     def displayDetails(self):
#         # accessing protected data members of parent class
#         print("Name: ", self._name)