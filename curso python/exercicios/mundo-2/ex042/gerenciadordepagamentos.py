print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input("Sua opção? "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('À vista o produto sai por R${:.2f} com 10% de desconto.'.format(total))
elif opcao == 2:
        total = preco - (preco * 5 / 100)
        print("À vista no cartão o produto sai por R${:.2f} com 5% de desconto.".format(total))
elif opcao == 3:
    total = preco 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${} com JUROS'.format(totalparcelas, parcela))
else:
    total = 0
    print('OPÇÂO INVÁLIDA. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

