salario = float(input("Qual é o salario do funcionario? R$ "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print("O funcionario que ganhava R${:.2f} passará a ganhar R${:.2f} agora".format(salario, novo))