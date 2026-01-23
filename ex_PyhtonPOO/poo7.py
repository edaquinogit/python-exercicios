class Smatwatch:
    def __init__(self):
        self.passos = 0
        self.meta = 1000

    def caminhar(self, quantidade):
        self.passos += quantidade
        print(f"Você caminhou {quantidade} passos total agora.")

    def verificar_meta(self):
        if self.passos >= self.meta:
            print("Meta batida! Voce é um Atleta!")
        else:
            faltam = self.meta - self.passos
            print(f"Ainda faltam {faltam} passos para sua meta de {self.meta}")

meu_relogio = Smatwatch()
meu_relogio.caminhar(400)
meu_relogio.verificar_meta()
meu_relogio.caminhar(700)
meu_relogio.verificar_meta()