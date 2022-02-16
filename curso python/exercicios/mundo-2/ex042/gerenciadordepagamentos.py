print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input("Sua opção? "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('á vista o produto sai por R${:.2f}'.format(total))
elif opcao == 2:
        total = preco - (preco * 5 / 100)
        print("á vista no cartao o produto sai por R${:.2f}".format(total))
elif opcao == 3:
    total = preco 
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${} com JUROS'.format(totalparcelas, parcela))
else:
    total = 0
    print('OPÇÂO INVÁLIDA. tente novamente!')

print('Sua compra de {} vai custar {} no final'.format(preco, total))

