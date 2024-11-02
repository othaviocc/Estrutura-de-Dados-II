class ListaCont():
    def __init__(self, max):
        self.max = max
        self.vector = [None] * self.max
        self.start = -1
        self.end = -1

    def __repr__(self):
        string = "[start"
        for i in range(self.max):
            string = string + " --> " + "[" + str(i +1) + "]" + " " + str(self.vector[i])
        return string + "]"

    def Empty(self):
        for i in self.vector:
            if (i != None):
                return False
        return True
    
    def Lenght(self):
        if self.Empty():
            return 0
        else:
            return self.end - self.start +1

    def Insert(self, pos, value):
        if (self.start -1 <= pos -1 <= self.end +1) and (None in self.vector) or self.Empty():
            if (self.Empty()):
                self.start = pos -1
                self.end = pos -1
            else:
                left = pos - self.start
                right = self.end - pos +2
                if (((right <= left) and (self.end +1 < self.max)) or self.start == 0):
                    for i in range(self.end, pos -2, -1):
                        self.vector[i +1] = self.vector[i]
                    self.end += 1
                else:
                    for i in range(self.start, pos):
                        self.vector[i -1] = self.vector[i]
                    self.start -= 1
            self.vector[pos -1] = value
            return True
        else:
            return False

    def Remove(self, pos):
        if (0 < pos <= self.max):
            left = pos -1 - self.start
            right = self.end - pos +1
            if (right <= left):
                for i in range(pos -1, self.end):
                    self.vector[i] = self.vector[i +1]
                self.vector[self.end] = None
                self.end -= 1
            else:
                for i in range(pos -1, self.start, -1):
                    self.vector[i] = self.vector[i -1]
                self.vector[self.start] = None
                self.start += 1
            return True
        else:
            return False

    def Busca(self, value, ini, fim):
        meio = (ini+fim)//2
        if ini == fim:
            return False
        if self.vector[ini] == value:
            return ini+1
        if self.vector[meio] >= value:
            self.Busca(value, ini, fim)
        else:
            return self.Busca(value, meio+1, fim)
        
    def BuscaBinaria(self, value):
        print(self.Busca(value, self.start, self.end))
        

    
    def Wipe(self):
        for i in range(self.max):
            self.vector[i] = None

l = ListaCont(10)
l.Insert(1, 1)
l.Insert(2, 2)
l.Insert(3, 3)
l.Insert(4, 4)
l.Insert(5, 5)
l.Insert(6, 6)
l.Insert(7, 7)
l.Insert(8, 8)
l.Insert(9, 9)
l.Insert(10, 10)

print(l)

l.BuscaBinaria(6)
