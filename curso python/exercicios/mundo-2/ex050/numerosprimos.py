número = int(input('Digite um número: '))
total = 0
for c in range(1, número + 1):
    if número % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(número, total))
if total == 2:
    print('Por isso ele É PRIMO')
else:
    print('Por isso ele NÃO é primo')