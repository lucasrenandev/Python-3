n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
média = (n1 + n2) / 2
print("A média do aluno é {}".format(média))
if média >= 7:
    print("O aluno está APROVADO!")
elif média < 7 and média >= 5:
    print("O aluno está em RECUPERAÇÂO!")
else:
    print("O aluno está REPROVADO.")