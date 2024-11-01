class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class PilhaEnc:
    def __init__(self):
        self.topo = None

    def Empilhar(self, dado):
        novo = Nodo(dado)
        if (not self.vazia()):
            novo.prox = self.topo
        self.topo = novo

    def Excluir(self):
        if (not self.vazia()):
            self.topo = self.topo.prox        

    '''def Excluir(self):
        if (not self.vazia()):
            aux = self.topo
            self.topo = aux.prox
            del aux'''

    def Consultar(self):
        if (not self.vazia()):
            return self.topo.info
        
    def Destruir(self):
        while (not self.vazia()):
            self.Excluir()