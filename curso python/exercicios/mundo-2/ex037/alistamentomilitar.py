from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print("Hora de se Alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda falta {} anos para o alistamento".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = saldo - atual
    print("Seu alistamento foi em {}".format(ano))