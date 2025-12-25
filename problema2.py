#  Exercicio de verificação de Media 

nome = input('Digite seu nome:')

print('Olá,{}! Bem vindo ao sistema de verificação de média.'.format(nome))
n1 = float(input('Digite sua Primeira Nota'))
n2 = float(input('Digite sua Segunda Nota'))
n3 = float(input('Digite sua terceira Nota'))
media = (n1 + n2 + n3) / 3
print()
if media >= 7:
    print('Parabens! Voce foi Aprovado com a media:{:.2f}'.format(media))
else:
    print('infelizmente voce foi Reprovado com a media:{:.2f}'.format(media))
print('Obrigado por ultilizar nosso sistema,{}!'.format(nome))