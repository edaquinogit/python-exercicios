# Exercicio de verificação de Saldo Bancario

nome = input('Digite seu nome:')

print('Ola{}, Seja bem vindo ao sistema bancario.'.format(nome)) 
saldo = float(input('Digite o saldo da sua conta bancaria: RS'))
print()
 
if saldo >= 0:
    print('Seu saldo é positivo! Saldo: RS{:.2f}'.format(saldo))
else:
    print('Seu Saldo é negativo! Saldo: RS{:.2f}'.format(saldo))

print()   

print('Obrigado {} por ultilizar nosso sistema bancario!'.format(nome))