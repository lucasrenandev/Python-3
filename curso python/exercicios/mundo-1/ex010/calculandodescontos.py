preço = float(input('Qual o preço do produto? R$ '))
desco = preço - (preço * 5 / 100)
print('O preço do produto é R${:.2f} com desconto de 5% ficará R${:.2f}.'.format(preço, desco))