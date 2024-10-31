class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class ListaEnc:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        ptAux = self.inicio
        while ptAux is not None:
            print(ptAux.info)
            ptAux = ptAux.prox

    def buscar(self, valorBuscado):
        ptAux = self.inicio
        while ptAux is not None:
            if ptAux.info == valorBuscado:
                print(ptAux.info, "encontrado")
                return
            ptAux = ptAux.prox
        print(valorBuscado, "não encontrado")

    def inserir(self, info, pos):
        novoNodo = Nodo(info)
        if pos == 0:  # Inserir no início
            novoNodo.prox = self.inicio
            self.inicio = novoNodo
        else:
            ptAux = self.inicio
            for _ in range(pos - 1):
                if ptAux is None:  # A posição é maior que o número de elementos na lista
                    print("Posição fora dos limites")
                    return
                ptAux = ptAux.prox
            if ptAux is None:  # Se a posição é no final da lista
                print("Posição fora dos limites")
                return
            novoNodo.prox = ptAux.prox
            ptAux.prox = novoNodo

    def remover(self, valorRemover):
        ptAux = self.inicio
        prev = None
        while ptAux is not None:
            if ptAux.info == valorRemover:
                if prev is None:
                    self.inicio = ptAux.prox
                else:
                    prev.prox = ptAux.prox
                del ptAux
                print(valorRemover, "removido")
                return
            prev = ptAux
            ptAux = ptAux.prox
        print(valorRemover, "não encontrado")


###################################################################################################3333


    def __str__(self):
        elementos = []
        ptAux = self.inicio
        while ptAux is not None:
            elementos.append(str(ptAux.info))
            ptAux = ptAux.prox
        return " -> ".join(elementos)

# Exemplo de uso:
lista = ListaEnc()
lista.inserir(10, 0)  # Inserir 10 no início
lista.inserir(20, 1)  # Inserir 20 no final
lista.inserir(30, 1)  # Inserir 30 no meio (posição 1)
lista.inserir(40, 3)  # Inserir 40 na última posição (posição 3)

print("Lista:")
print(lista)

print("Buscando 20:")
lista.buscar(20)

print("Removendo 20:")
lista.remover(20)

print("Lista após remoção:")
print(lista)

print("Buscando 20 novamente:")
lista.buscar(20)


    

