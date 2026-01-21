#exercicio do carro

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} foi ligado")
        
    def acelerar(self):
        if self.ligado == True:
            self.velocidade += 10
            print(f"Seu {self.modelo} esta acelerando!")
        else:
            print(f"O {self.modelo} não esta ligado")
        
    def exibir_painel(self):
        print(f"Seu {self.modelo} esta em {self.velocidade:.2f} km/h")

carro1 = Carro("Uno")

carro1.ligar()
carro1.acelerar()
carro1.acelerar()
carro1.exibir_painel()