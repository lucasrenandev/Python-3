from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento do atleta? '))
idade = atual - nasc
print('O atleta nasceu em {} e tem {} anos.'.format(nasc, idade))
if idade <=9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
    