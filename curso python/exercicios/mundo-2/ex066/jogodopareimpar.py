from random import randint
totvitórias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}! Um total de {total},', end= ' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            totvitórias += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            totvitórias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...? ')
print(f'GAME OVER! Você venceu {totvitórias} vezes!')