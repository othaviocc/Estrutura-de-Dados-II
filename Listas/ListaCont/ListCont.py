class Lista:
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def Inserir(self, posicao, dado):
        if (self.ini != 0 or self.fim != self.max -1) and posicao> 0 and posicao <= self.tamanho()+1: # verificar se existe espaço e se a posição é válida
            if (self.vazia()):
                self.ini = 0
                self.fim = 0
            elif (self.fim != self.max - 1): # deslocar para o fim
                for i in range(self.fim, self.ini + posicao -2, -1):
                    self.vetor[i+1] = self.vetor[i]
                    print("moveu")
                self.fim = self.fim + 1
            else: # deslocar para o início,  como ja esta cheia, eu tiro o primeiro elemento
                for i in range(self.ini, self.ini + posicao):
                    self.vetor[i-1] = self.vetor[i]
                    print("moveu")
                self.ini = self.ini - 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        else:
            return False
        
    def consultar(self, posicao):
        if not(self.vazia()):
            return self.vetor[self.ini + posicao - 1]
    
    def vazia(self):
        return self.ini == -1 or self.fim == -1
    
    def tamanho(self):
        if self.vazia():
            return 0
        else:
            return self.fim - self.ini + 1
        
    def limpar(self):
        self.ini = -1
        self.fim = -1
    def excluir(self, posicao):
        if self.vazia() or posicao <= 0 or posicao > self.tamanho():
            return False
        if self.ini == self.fim:
            # Lista com um único elemento
            self.ini = -1
            self.fim = -1
        elif posicao == 1:
            # Remover o primeiro elemento
            for i in range(self.ini, self.fim):
                self.vetor[i] = self.vetor[i + 1]
            self.fim -= 1
        elif posicao == self.tamanho():
            # Remover o último elemento
            self.fim -= 1
        else:
            # Remover um elemento do meio
            for i in range(self.ini + posicao - 1, self.fim):
                self.vetor[i] = self.vetor[i + 1]
            self.fim -= 1
        
        return True




###################################################################
    def __repr__(self):   #APENAS PARA FAZER O EXEMPLO
        string = "[ini  "
        for i in range(self.ini, self.fim + 1):
            string = string + " ---> " +str(self.vetor[i])
        return string + "]"

####################################################################
