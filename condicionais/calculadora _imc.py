print("Calculadora de IMC")
print("Vamos calcular o seu Índece de Massa Corporal (IMC)")
print()

#Entrada de dados do usuario
nome = str(input("Digite seu nome:"))
altura = float(input("Digite sua altura em metros:"))
peso =  int(input("Digite seu peso em KG:"))
print()

#Calculo do IMC

imc = peso / (altura * altura)

resultado = imc
#Classificando o IMC atraves de funções e de condicionais
def classificar_imc(resultado):
    if resultado < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= resultado < 24.9:
        return "Peso normal"
    elif 25 <= resultado < 29.9:
        return "Sobrepeso"
    elif 30 <= resultado < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= resultado < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

def peso_ideal(classificar_imc):
    if classificar_imc == "Peso normal":
        return(nome) + "Voce está com o peso ideal. Parabéns!"
    else:
        return(nome) + "Você não está com o peso ideal. Vamos cuidar da saúde!"
    
#Exibincdo os resultados

print("Olá,{nome}! Seu IMC é de {resultado:.2f},"
     .format(nome=nome, resultado=resultado, classificar_imc=classificar_imc, peso_ideal=peso_ideal(classificar_imc)))
print("Classificação do IMC:", classificar_imc(resultado))
   