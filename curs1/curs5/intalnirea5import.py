#Importare functii din alte fisiere

# import intalnirea5continuare
# varsta = 17
# pret = 200
# print(intalnirea5continuare.calcul_pret_bilet(varsta, pret))
#
#alta varianta
# from intalnirea5continuare import *
# varsta = 17
# pret = 200
#
# print(calcul_pret_bilet(varsta, pret))

#alta varianta - import doar o functie
from intalnirea5continuare import calcul_pret_bilet
varsta = 15
pret = 200
print(calcul_pret_bilet(varsta, pret))