class Nodo():
    def __init__(self, value):
        self.data = value
        self.next = None

class ListaEnc:
    def __init__(self):
        self.start = None
        self.length = 0

    def __repr__(self):
        aux = self.start
        string = "[ ini "
        for i in range(self.length):
            string += f"--> Value: {aux.data} "
            aux = aux.next
        return string + "]"
    
    def Insert(self, pos, value):
        if (self.length == 0): #Inserir nodo em lista vazia
            nodo = Nodo(value)
            self.start = nodo
            self.length += 1
            return True
        elif (pos == 1): #Inserir nodo no comeco da lista
            nodo = Nodo(value)
            nodo.next = self.start
            self.start = nodo
            self.length += 1
            return True
        elif (1 < pos <= self.length): #Inserir nodo no meio da lista
            aux = self.start
            aux2 = aux.next
            for i in range(pos -2):
                aux = aux2
                aux2 = aux2.next
            nodo = Nodo(value)
            nodo.next = aux2
            aux.next = nodo
            self.length += 1
            return True
        elif (pos == self.length +1): #Inserir nodo no final da lista
            aux = self.start
            for i in range(self.length -1):
                aux = aux.next
            nodo = Nodo(value)
            aux.next = nodo
            self.length += 1
            return True
        return False
    
    def ConsulRec(self, value, cont, nodo):
        if (nodo.data == value):
            return cont
        elif (nodo.next == None):
            return False
        else:
            return self.ConsulRec(value, cont+1, nodo.next)

    def Consult(self, value):
        print(self.ConsulRec(value, 0, self.start))
            

l = ListaEnc()
l.Insert(1, 5)
l.Insert(2, 12)
l.Insert(3, 52)
l.Insert(4, 15)
print(l)

l.Consult(5)