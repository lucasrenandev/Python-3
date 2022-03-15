print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Qual o valor a ser sacado? R$  '))
total = valor
cédula = 50
totcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totcédula += 1
    else:
        if totcédula > 0:
            print(f'Total de {totcédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totcédula = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')