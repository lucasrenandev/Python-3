resposta = 'S'
soma = quantidade = média = maior = menor = 0
while resposta in 'Ss':
    número = int(input('Digite um número: '))
    soma += número
    quantidade += 1
    if quantidade == 1:
        maior = número
        menor = número
    else:
        if número > maior:
            maior = número
        elif número < menor:
            menor = número

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quantidade
print('Ao todo foram {} valores informados e a média entre eles foi {:.2f}'.format(quantidade, média))
print('O maior valor informado foi {} e o menor foi {}'.format(maior, menor))

print('Fim do programa!')