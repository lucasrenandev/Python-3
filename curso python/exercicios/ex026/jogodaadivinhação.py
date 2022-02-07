from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print("Vamos jogar! Pensando em um número entre 0 e 5. Tente adivinhar... ")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3) 
if jogador == computador:
    print("PARABÉNS! Você acertou!")
else:
    print("Ganhei! O número em que pensei foi {} e não {}!".format(computador, jogador))