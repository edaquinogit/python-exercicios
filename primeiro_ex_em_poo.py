print("\nPrimeiro exemplo em poo python\n")

# Definindo classes e objetos em python

class Tarefa:
    def __init__(self, nome, data, prioridade):
        self.nome = nome
        self.data = data
        self.prioridade = prioridade
        self.concluida = False

    def finalizar(self):
        self.concluida = True
# Exibindo os detalhes da tarefa
    def exibir(self):
        status = "Concluída" if self.concluida else "Pendente"
        print(f"Tarefa: {self.nome}\n"
              f"Data: {self.data}\n"
              f"Prioridade: {self.prioridade}\n"
              f"Status: {status}\n") 
# Criando um objeto da classe Tarefa
t1 = Tarefa("Estudando POO", "2026/01/15", "Alta")
t1.exibir()
print("-"*30)
print("finalizando a tarefa")
t1.finalizar()
print("-"*30)
