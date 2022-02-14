real = float(input('Digite quanto dinheiro voçê tem na carteira: '))
dolar = real / 3.27
euro = real / 6.40
print('Com R${:.2f} você pode comprar US${:.2f} e £{:.2f}'.format(real, dolar, euro ))
