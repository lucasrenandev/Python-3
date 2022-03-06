from time import sleep


n1 = int(input('Primeiro valor: ')) 
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('O que deseja fazer? ')
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}!'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('O resultado de {} x {} é igual a {}!'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}!'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os valores: ')
        n1 = int(input('Primeiro valor: ')) 
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Valor inválido! Tente novamente.')
    print('=-=' * 10)
    sleep(3)


print('Fim do programa! Volte sempre.')
