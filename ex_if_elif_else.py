
# if / elif  / else
#se / se não / caso contrario

print("Seja bem vindo ao sistema de verificação de idade!")
print()

nome = input("Digite seu nome:")
print()
print("Olá, {nome}!".format(nome=nome), "vamos verificar sua idade!")
print()

idade = input("digite sua idade:")
mostrar_idade = int(idade)
print()
print("Você tem {idade} anos de idade.".format(idade=mostrar_idade))
print()

variacao_idade = int(idade)

if variacao_idade < 18:
    print("Você é menor de idade!")
elif variacao_idade >= 18 and variacao_idade < 20:
    print("Você é Maior de Idade!")
elif variacao_idade >= 20 and variacao_idade < 60:
    print("Você é adulto!")
else:
    print("Você é idoso!")

print()

print("Obrigado por utilizar nosso sistema de verificação de idade!")