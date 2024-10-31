from Carro import *
from ListCont import *

carroA = Carro("AAAAA", 1111)
carroB = Carro("BBBBB", 2222)
carroC = Carro("CCCCC", 3333)


lista = Lista(9)
if (lista.Inserir(1, carroA)):
    print(lista)
if (lista.Inserir(2, carroC)):
    print(lista)
if (lista.Inserir(1, carroB)):
    print(lista)
if (lista.Inserir(5, carroA)):
    print(lista)
if (lista.Inserir(5, carroB)):
    print(lista)

#Excluir = lista.excluir(3)
#print(lista)
'''
meuCarro = lista.consultar(1)
print(meuCarro)'''