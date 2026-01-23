class Gafanhoto:
    """
    Aprendendo a documentar com o __doc__ (serve como um manual para o programador)

    essa classe cria um gafanhoto que tem nome e idade
    para cria uma nova pesoa, use 
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "Vazio", idade = 0):
        self.nome = nome
        self.idade = int(idade)

#metodo de instancia    
    def aniversario(self):
          self.idade += 1
    
    def __str__(self): #Dunder Method
         return f"{self.nome} é Gafonhoto e tem {self.idade} anos de idade."
    
    def __getstate__(self):
         return f"Estado: nome = {self.nome}: idade = {self.idade}"
    


# Declaracao do objeto (instanciando)
g1 = Gafanhoto("Maria", 18)
g1.aniversario()
print(g1.__str__()) #Atribute
print(g1.__getstate__()) #method
#print(g1.__class__) ve a classe do objeto
#print(g1.__doc__) #Dunder Attribute
print(g1.__dict__)


g2 = Gafanhoto()
g2.aniversario()
print(g2.__str__())
print(g2.__getstate__())