# input preço
# input condição de pagamento
# à vista (dinheiro ou cheque) - 10% desconto
# à vista (cartao de crédito) - 5% desconto
# crédito (até 2x) - preço normal
# crédito (3x ou mais) - 20% juros

print('-=-' * 15)
print(f'{"Lojas Guanabara":^45}')
print('-=-' * 15)
valor = float(input('Informe o valor da compra: R$ '))
opcao = int(input('''
Informe a opção de pagamento:
[1] à vista (dinheiro ou cheque)
[2] à vista (cartão de crédito)
[3] cartão de cŕedito (até 2x) 
[4] cartão de crédito (3x ou mais)
opção: '''))
print(f'O valor a ser pago é R$ ', end='')
if opcao == 1:
    print(f'{valor*0.9:.2f}'.replace('.', ','))
elif opcao == 2:
    print(f'{valor * 0.95:.2f}'.replace('.', ','))
elif opcao == 3:
    print(f'{valor:.2f}'.replace('.', ','))
    print(f'2 x R$ {valor/2}'.replace('.', ','))
elif opcao == 4:
    print(f'{valor * 1.2:.2f}'.replace('.', ','))
    for c in range(3, 13):
        print(f' - {c} x R$ {(valor * 1.2)/c:.2f}'.replace('.', ','))
else:
    print('Opção inválida')
