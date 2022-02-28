somaidade = 0
médiaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadedehomem, nomevelho))
print('Ao todo são {} Mulheres com menos de 20 anos.'.format(totmulher20))