class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100

    def correr(self):
        if self.energia >= 20:
            self.energia -= 20
            print(f"{self.nome} correu! Perdeu 20 de energia.")
        else:
            print(f"O jogador está cansado para correr!")

    
    def comer(self):
        if self.energia <= 90:
            self.energia += 10
            print(f"{self.nome} comeu e recuperou 10 de energia.")
        else:
            self.energia = 100
            print(f"{self.nome} ja está cheio!")


    def mostrar_status(self):
        print(f"Status atual -> Nome: {self.nome} | Energia: {self.energia}")


# Jogando pro terminal:

nome_do_player = input("Qual o nome do seu Personagem?")
jogador1 = Jogador(nome_do_player)

jogador1.mostrar_status()
jogador1.correr()
jogador1.correr()
jogador1.comer()
jogador1.mostrar_status()

