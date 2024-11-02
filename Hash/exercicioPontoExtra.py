"""
Considerando o TAD tabela hash com função hash resto da divisão, tratamento de colisão opening adressing com pesquisa linear e encadeamento, implementa a operação de exclusão.
Dica: percorrer todos os encadeamentos e sobrescrever valores do fim para o início.
"""
class Tabela:
    def __init__(self, size):
        self.primeNumber = self._primeNumber(size)
        self.vector = [None] * self.primeNumber
        self.free = self.primeNumber
        for i in range(self.primeNumber):
            self.vector[i] = [None, None, None]

    def __repr__(self):
        output = '\n'
        for i in range(self.primeNumber):
            output += str(i) + ': '
            if self.vector[i][0] != None:
                output += str(self.vector[i][0]) + ' -> ' + str(self.vector[i][1]) + ' -> ' + str(self.vector[i][2])
            output += '\n'
        return output[:len(output)-2]

    def _insert(self, key, value):
        index = self._transformStringToKey(key) % self.primeNumber
        if self.vector[index][0] == None:
            self.vector[index][0], self.vector[index][1] = key, value
            self.free -= 1
            return True
        if self._changeValue(key, value, index): return True
        if self.free == 0: return False
        if self._insertAndChain(key, value, index): return True
        return self._changeIndex(key, value, index)

    def _changeValue(self, key, value, index):
        try:
            while True:
                if self.vector[index][0] == key:
                    self.vector[index][1] = value
                    return True
                index = self.vector[index][2]
        except TypeError:
            return False

    def _insertAndChain(self, key, value, index):
        if self._verifyHash(index):
            lastRow = index
            while True:
                if self.vector[lastRow][2] == None:
                    break
                lastRow = self.vector[lastRow][2]
            for i in range(self.primeNumber):
                i = (i + index) % self.primeNumber
                if self.vector[i][0] == None:
                    self.vector[i][0], self.vector[i][1]  = key, value
                    self.vector[lastRow][2] = i
                    self.free -= 1
                    return True
        return False

    def _changeIndex(self, key, value, index):
        oldIndex = [self._transformStringToKey(self.vector[index][0]) % self.primeNumber]
        for i in range(self.primeNumber):
            if self.vector[oldIndex[i]][2] == None:
                break
            oldIndex.append(self.vector[oldIndex[i]][2])
        for i in range(self.primeNumber):
            i = (i + oldIndex[len(oldIndex) - 1]) % self.primeNumber
            if self.vector[i][0] == None:
                self.vector[oldIndex[len(oldIndex) - 1]][2] = i
                oldIndex.append(i)
                break
        for i in range(len(oldIndex) - 1, -1, -1):
            if oldIndex[i] % self.primeNumber == index:
                self.vector[oldIndex[i - 1]][2] = oldIndex[i + 1]
                break
            self.vector[oldIndex[i]][0], self.vector[oldIndex[i]][1]  = self.vector[oldIndex[i - 1]][0], self.vector[oldIndex[i - 1]][1]
        self.vector[index][0], self.vector[index][1], self.vector[index][2] = key, value, None
        self.free -= 1
        return True

    def _verifyHash(self, index):
        if self._transformStringToKey(self.vector[index][0]) % self.primeNumber == index:
            return True
        return False

    def _remove(self, key):
        try:
            index = self._transformStringToKey(key) % self.primeNumber
            behindRow = None
            row = index
            nextRow = self.vector[row][2]
            while True:
                if self.vector[row][0] == key:
                    break
                behindRow = row
                row = nextRow
                nextRow = self.vector[row][2]
        except TypeError:
            return False
        while True:
            if nextRow == None:
                break
            self.vector[row][0], self.vector[row][1] = self.vector[nextRow][0], self.vector[nextRow][1]
            behindRow = row
            row = nextRow
            nextRow = self.vector[row][2]
        self.vector[behindRow][2] = None
        self.vector[row] = [None, None, None]
        return True

    def _search(self, key):
        try:
            index = self._transformStringToKey(key) % self.primeNumber
            while True:
                if self.vector[index][0] == key:
                    return (index, self.vector[index][1])
                index = self.vector[index][2]
        except TypeError:
            return False

    @staticmethod
    def _transformStringToKey(key):
        try:
            key = int(key)
            return key
        except ValueError:
            return ord(key[0])

    @staticmethod
    def _primeNumber(number):
        while True:
            if ((number % 2 != 0) and (number % 3 != 0) and (number % 5 != 0)) and (number != 0 and number != 1) or (
                    number == 2 or number == 3 or number == 5):
                return number
            number += 1
