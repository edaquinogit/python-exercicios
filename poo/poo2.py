class Usuario:
    def __init__(self, nome_inicial, senha_inicial):
        self.nome = nome_inicial
        self.senha = senha_inicial
        self.saldo = 0.0

    def mostrar_saldo(self):
        print(f"Olá, {self.nome}, seu saldo atual é R${self.saldo:.2f}")

    def depositar(self, valor_depositado):
        if valor_depositado > 0:
            self.saldo += valor_depositado
        else:
            print("ERRO: O valor do deposito deve ser maior de zero.")

    def saque(self, valor_sacado):
        if valor_sacado > 0:
            valor_sacado - self.saldo
        else:
            print("Saque de {valor_sacado:.2f} realizado com Sussesso")

    def mostrar_saldo_saque(self):
        print(f"Olá {self.nome}, atualmente seu saldo é {self.saldo:.2f}")

user_nome = input("Crie seu nome de usuario:")
user_senha = input("Crie sua senha:")
pessoa1 = Usuario(user_nome, user_senha)
pessoa1.mostrar_saldo()


valor = float(input("Quanto deseja deposita?"))
pessoa1.depositar(valor)
pessoa1.mostrar_saldo()

saque = float(input("Quanto deseja Sacar?"))
pessoa1.saque(valor)
pessoa1.mostrar_saldo_saque()

