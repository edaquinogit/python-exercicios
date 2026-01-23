# Simulação de automatização de cafeteira

class Cafeteira():
    def __init__(self):
        self.valor = 5
        self.agua_atual = 400
        self.ligada = False
        
    def ligar_desligar(self):
        self.ligada = not self.ligada
        status = "ligada" if self.ligada else "desligada"
        print(f"A maquina agora está {status}.")

    def fazer_cafe(self):
        if not self.ligada:
            print("Erro: A maquina está desligada!")
            return
        if self.agua_atual >= 100:
            self.agua_atual -= 100
            print(f"Cafe preparado! Custo: R${self.valor}. Restam {self.agua_atual}ml de agua")

    def reabastecer(self):
        self.agua_atual = 400
        print("Reservatorio abastecido com 400ml")



cafe1 = Cafeteira()
cafe1.ligar_desligar()
cafe1.fazer_cafe()
cafe1.fazer_cafe()
cafe1.fazer_cafe()
cafe1.fazer_cafe()
cafe1.reabastecer()


        