import moeda
p = float(input('Digite o preço: R$ '))
print (f'A metade de R$ {p} é {moeda.metade(p)}.')
print(f'O dobro de R$ {p} é {moeda.dobro(p)}.')
print(f'Amentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Diminuindo 20%, temos R$ {moeda.diminuir(p, 20)}')

