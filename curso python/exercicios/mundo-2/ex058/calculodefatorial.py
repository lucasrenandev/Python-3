# Usando o comando (WHILE)

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(c), end=' ')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

# Usando o comando (FOR)
'''
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(c), end=' ')
for c in range (c, 0, -1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
print('{}'.format(f))'''