# Exercicio de verificação de idade

print('Bem vindo ao sistema de verificação de idade!')

print()

nome = input('Digite seu nome:')
print('Olá,{}!'.format(nome))

print()

n1 = float(input('Digite sua idade:'))
if n1 >= 18:
   print('Acesso permitido! Voce é maior de idade.')
else:
    print('Acesso negado!Voce é menor de idade')

print()

print('Obrigado por ultilizar noss o sistema de verificação de idade,{}!'.format(nome))