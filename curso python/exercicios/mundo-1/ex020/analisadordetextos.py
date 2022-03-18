from time import sleep

nome = str(input("Digite seu nome completo: ")).strip()
print('ANALISANDO SEU NOME...')
sleep(2)
print('Seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))