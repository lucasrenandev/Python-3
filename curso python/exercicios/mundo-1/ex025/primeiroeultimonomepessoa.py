nome = str(input('Digite seu nome: ')).strip()
ultnome = nome.split()
print('Seu primeiro nome é {}'.format(ultnome[0]))
print('Seu ultimo nome é {}'.format(ultnome[len(ultnome)-1]))
