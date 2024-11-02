class Conta:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial

    def get_saldo(self):
        return self.saldo

    def debito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do débito deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o débito.")
        self.saldo -= valor

    def credito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do crédito deve ser positivo.")
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        if not isinstance(conta_destino, Conta):
            raise TypeError("O destino deve ser uma instância de Conta.")
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        self.debito(valor)
        conta_destino.credito(valor)
        print(f"Transferência de {valor} realizada com sucesso.")

# Exemplo de uso
if __name__ == "__main__":
    conta1 = Conta(numero=123, titular="Alice", saldo_inicial=500)
    conta2 = Conta(numero=456, titular="Bob", saldo_inicial=300)

    print(f"Saldo inicial da conta 1: {conta1.get_saldo()}")
    print(f"Saldo inicial da conta 2: {conta2.get_saldo()}")

    conta1.transferir(200, conta2)

    print(f"Saldo final da conta 1: {conta1.get_saldo()}")
    print(f"Saldo final da conta 2: {conta2.get_saldo()}")
