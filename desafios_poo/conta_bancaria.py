class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta criada {self.id} criada com sussesso! atualmente seu saldo é {saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem {self.saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        self.saldo += valor 
        print(f"Seu deposito de {valor:,.2f} foi realizado com susseso na conta {self.id}.")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.id} Saldo insuficiente")
        else:
            self.saldo -= valor
        print(f"Saque de RS{valor:,.2f} autorizado na conta {self.id} com sussesso!")

# Criacao e uso do objeto

c1 = ContaBancaria(113, "Ednaldo", 4000)
c1.depositar(500)
c1.sacar(3000)
print(c1)
