peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
   
