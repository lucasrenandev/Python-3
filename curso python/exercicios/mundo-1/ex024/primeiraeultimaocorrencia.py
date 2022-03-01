frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')))   #find(encontrar, procurar)
print('Ela aparece pela ultima vez na posição {}'.format(frase.rfind('A')))  #rfind(encontrar, procurar do lado direito)