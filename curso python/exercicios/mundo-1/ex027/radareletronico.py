velocidade = float(input("Qual é a velocidade do carro? "))
if velocidade > 80:
    print("Multado! Você excedeu o limite permitido que é de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Voçê deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um Bom dia! Dirija com segurança!")
    