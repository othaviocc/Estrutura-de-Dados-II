class Nodo:
    def __init__(self, chave, info):
        self.info = info
        self.chave = chave
        self.esq = None
        self.dir = None

    def folha(self):
        return self.esq is None and self.dir is None
    
    def ladoFilho(self):
        if self.esq and self.dir is None:
            return "esq"
        elif self.esq is None and self.dir:
            return "dir"
        elif self.esq and self.dir:
            return "ambos"
    
    def ins(self, chave, valor):
        if  chave > self.chave:
            if self.dir is None:
                self.dir = Nodo(chave, valor)
                return chave
            else: 
                return self.dir.ins(chave, valor)
        elif chave < self.chave:
            if self.esq is None:
                self.esq = Nodo(chave, valor)
                return chave
            else:
                return self.esq.ins(chave, valor)
        else:
            return None
        
    def bus(self, chave):
        if chave == self.chave:
            return self.info
        elif chave < self.chave:
            if self.esq:
                return self.esq.bus(chave)
        elif chave > self.chave:
            if self.dir:
                return self.dir.bus(chave)
        return None
    
    def localizaPai(self, chave, pai = None):
        if chave == self.chave:
            return pai
        elif chave < self.chave:
            if self.esq:
                return self.esq.localizaPai(chave, self)
        elif chave > self.chave:
            if self.dir:
                return self.dir.localizaPai(chave, self)
        return None
    
    def rem(self, chave):
        pai = self.localizaPai(chave)
        if pai:
            if pai.esq and pai.esq.chave == chave:
                if pai.esq.folha():
                    pai.esq = None
                elif pai.esq.ladoFilho == "esq":
                    pai.esq = pai.esq.esq
                elif pai.esq.ladoFilho == "dir":
                    pai.esq = pai.esq.dir
                else:
                    sucessor = pai.esq.dir
                    while sucessor.esq:
                        sucessor = sucessor.esq
                    pai.esq.chave = sucessor.chave
                    pai.esq.info = sucessor.info
                    pai.esq.dir.rem(sucessor.chave)

            elif pai.dir and pai.dir.chave == chave:
                if pai.dir.folha():
                    pai.dir = None
                elif pai.dir.ladoFilho() == "esq":
                    pai.dir = pai.dir.esq
                elif pai.dir.ladoFilho() == "dir":
                    pai.dir = pai.dir.dir
                else:
                    sucessor = pai.dir.dir
                    while sucessor.esq:
                        sucessor = sucessor.esq
                    pai.dir.chave = sucessor.chave
                    pai.dir.info = sucessor.info
                    pai.dir.dir.rem(sucessor.chave)
    
    def altura(self):
        pass

    def remSubMaiorAlt(self,):
        pass

class ABP:
    def __init__(self):
        self.raiz = None

    def insere(self, chave, valor):
        if self.raiz is None:
            self.raiz = Nodo(chave, valor)
            return chave
        else:
            return self.raiz.ins(chave, valor)
            
    def busca(self, chave):
        if self.raiz:
            return self.raiz.bus(chave)
        else:
            return None

    def remove(self, chave):
        if self.raiz.folha() and self.raiz.chave == chave:
            self.raiz = None
            return chave
        else:
            return self.raiz.rem(chave)

arv = ABP()
arv.insere(30, "300")
arv.insere(26, "260")
arv.insere(29, "290")
arv.insere(70, "700")
arv.insere(52, "520")
arv.insere(7, "70")

arv.remove(26)
print(arv.busca(29))

