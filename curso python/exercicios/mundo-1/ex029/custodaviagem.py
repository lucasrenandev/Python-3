distancia = float(input("Qual a distância da viagem? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("E o preço da passagem será de R${:.2f}".format(preco))

#distancia = float(input("Qual a distancia da viagem? "))
#print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#print("E o valor da viagem será de R${:.2f}".format(preco))


