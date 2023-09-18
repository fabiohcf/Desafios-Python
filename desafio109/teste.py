from desafio109 import moeda
p = float(input('Digite o preço: R$ '))
print (f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}.')
print(f'Amentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 20%, temos {moeda.diminuir(p, 20)}')

