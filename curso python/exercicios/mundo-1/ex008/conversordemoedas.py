real = float(input('Quanto de dinheiro você quer converter: R$  '))
dolar = real / 5.16
euro = real / 5.73
print('Com R${:.2f} você pode comprar US${:.2f} e £{:.2f}'.format(real, dolar, euro ))
