soma = valores = 0
while True:
    num = int(input('Digite um número (999 para parar):  '))
    if num == 999:
        break
    valores += 1
    soma += num

print(f'A soma dos {valores} valores digitados é {soma}!')