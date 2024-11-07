class Arvore:
    def __init__(self, dado):
        self.esq = None
        self.info = dado
        self.dir = None

    def imprimir_PreEsq(self):  #Pre fixado a esquerda
        print(self.info)
        if self.esq != None:
            self.esq.imprimir_PreEsq()
        if self.dir != None:
            self.dir.imprimir_PreEsq()

    def infixDir(self):   
        if self.dir != None:
            self.dir.infixDir()
        print(self.info)
        if self.esq != None:
            self.esq.infixDir()

    def localizar(self, valor):    #LocalizaPai
        if self != None:
            if valor == self.info:
                return self
            if self.esq:
                aux = self.esq.localizar(valor)
                if aux:
                    return aux
            if self.dir:
                aux = self.dir.localizar(valor)
                if aux:
                    return aux
            return None

    def inserir(self, pai, filho, lado):
        pai = self.localizar(pai)
        if lado == "esq":
            if pai.esq == None:
                pai.esq = Arvore(filho)
        if lado == "dir":
            if pai.dir == None:
                pai.dir = Arvore(filho)

    def excluir(self, P, lado ):
        pai = self.localizar(P)
        if lado == 'esq':
            if pai.esq:
                pai.esq = None
        if lado == 'dir':
            if pai.dir:
                pai.dir = None

    def folha(self):
        return (self.esq == None and self.dir == None)

    def removerfolha(self, valor):
        nodoPai = self.localizar(valor)
        if (nodoPai):
            if (nodoPai.esq and nodoPai.esq.info == valor and nodoPai.esq.folha()):
                nodoPai.esq = None
            if (nodoPai.dir and nodoPai.dir.info == valor and nodoPai.dir.folha()):
                nodoPai.dir = None
    

a= Arvore("A")
a.esq = Arvore("B")
a.dir = Arvore("C")
a.esq.esq = Arvore("D")
a.esq.esq.dir = Arvore("E")
a.esq.esq.esq = Arvore("F")
a.esq.dir = Arvore("G")
a.imprimir_PreEsq()

print("================")
p = a.localizar("H")
print(p)
print("================")

a.inserir("G","W","esq")
a.imprimir_PreEsq()




