#declaração de classe 
class Gafanhoto:
    def __init__(self):
        self.nome = "" # atributos
        self.idade = 0

#metodo de instancia    
    def aniversario(self):
          self.idade == 0

    def mensagem(self):
         return f"{self.nome} é Gafonhoto(a) e tem {self.idade} anos de idade."
    
# Declaracao do objeto (instanciando)
g1 = Gafanhoto()
g1.nome = "Ednaldo"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "joao"
g2.idade = 18
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = "Maria"
g3.idade = 19
g3.aniversario()
print(g3.mensagem())

g4 = Gafanhoto()
g4.nome = "jose"
g4.idade = 28
print(g4.mensagem())