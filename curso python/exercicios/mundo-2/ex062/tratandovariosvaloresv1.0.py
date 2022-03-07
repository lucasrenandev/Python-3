número = cont = soma = 0
número = int(input('Digite um número [999 para parar] '))
while número != 999:
    soma += número
    cont += 1
    número = int(input('Digite um número [999 para parar] '))
print('Ao todo foram {} números digitados e a soma entre eles foi {}.'.format(cont, soma))

print('Fim do programa!')