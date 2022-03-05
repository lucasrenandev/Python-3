from random import randint

computador = randint(0, 10)
print('Olá, Sou seu computador... Estou pensando em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual é?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tenta mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('ACERTOU !!!')
print('Você acertou em {} tentativas.'.format(palpite))
