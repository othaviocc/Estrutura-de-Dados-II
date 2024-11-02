class Pilha:
    def __init__(self):
        self.itens = []
    
    def vazia(self):
        return self.itens == []
    
    def inserir(self, item):
        self.itens.append(item)
    
    def pop(self):
        if not self.vazia():
            return self.itens.pop()
   
    def tamanho(self):
        return len(self.itens)


class Fila:
    def __init__(self):
        self.pilha1 = Pilha()  # Pilha para operações de enqueue
        self.pilha2 = Pilha()  # Pilha para operações de dequeue
    
    def Vazia(self):
        return self.pilha1.vazia() and self.pilha2.vazia()
    
    def enqueue(self, item):
        self.pilha1.inserir(item)
    
    def dequeue(self):
        if self.pilha2.vazia():
            while not self.pilha1.vazia():
                self.pilha2.inserir(self.pilha1.pop())
        return self.pilha2.pop()
    
    def TamanhoFila(self):
        return self.pilha1.tamanho() + self.pilha2.tamanho()
    
    def ordenar(self):
        Paux = Pilha()
        
        while not self.Vazia():
            tmp = self.dequeue()
            while not Paux.vazia() < tmp: 
                self.enqueue(Paux.pop())
            Paux.inserir(tmp)
        
        # Copia os elementos ordenados de volta para a fila original
        while not Paux.vazia():
            self.enqueue(Paux.pop())


#teste
fila = Fila()
fila.enqueue(5)
fila.enqueue(2)
fila.enqueue(9)
fila.enqueue(1)
fila.enqueue(5)
fila.ordenar()
while not fila.Vazia():
    print(fila.dequeue(), end=' ')
print()
