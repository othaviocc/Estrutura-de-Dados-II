class nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = nodo

class FilaEnc:
    def __init__(self):
        self.tam = 0
        self.ini = None
        self.fim = None

    def consultar(self):
        #Se ela esta vazia
        if self.tam > 0:          
            return self.ini.info
        else:
            return None
        
    def inserir(self, valor):
        elem = nodo(valor)
        #Se ela esta vazia
        if self.tam == 0:         
            self.ini = elem
        else:                        
            self.fim.prox = elem
        
        self.fim = elem
        self.tam += 1

    def remover(self):
        #Se ela não esta vazia
        if self.tam > 0:         
            jet = self.ini.info
            self.ini = self.ini.prox
            if self.tam == 1:
                self.fim = None

            self.tam -= 1
            return jet
        else:
            return None
    
    def destruir(self):
        #Se ela não esta vazia
        while self.tam > 0:         
            self.excluir()
    
F= FilaEnc()
