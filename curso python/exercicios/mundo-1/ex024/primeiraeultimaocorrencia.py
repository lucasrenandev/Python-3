from re import A


frase = str(input('Digite uma frase: ')).upper()
print('A letra a aparece {} vezes na frase'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')))   ##find(encontrar)
print('Ela aparece a ultima vez na posição {}'.format(frase.rfind('A')))