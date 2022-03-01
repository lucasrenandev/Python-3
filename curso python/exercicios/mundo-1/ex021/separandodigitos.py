from time import sleep

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
sleep(2)
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))