salario = float(input('Qual o salário do funcionário: R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f} com 15% de aumento passará a receber R${:.2f}'.format(salario, novo))
