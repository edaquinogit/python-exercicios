class Cofre:
    def __init__(self):
        self.nome = ""
        self.valor = 0
        self.inteiro = True

    def depositar(self, valor):
        if self.inteiro == True:
            self.valor += valor
        else:
            print(f"Erro! O cofre foi quebrado e não aceita mais deposito")

    def quebrar(self):
        self.inteiro = False
        print(f"Olá {self.nome}, seu saldo atual é {self.valor}!")
        return

meu_porquinho = Cofre()
meu_porquinho.nome = "Ednaldo"
meu_porquinho.depositar(60)
meu_porquinho.quebrar()
meu_porquinho.depositar(20)
meu_porquinho.quebrar
