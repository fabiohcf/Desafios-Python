# caixa eletrônico  para saque, células disponíveis 50, 20, 10, 1

from time import sleep

print('-' * 30)
print(f'{"BANCO TOCA":^30}')
print('-' * 30)
valor = float(input('Qual valor deseja sacar?\nR$ ').replace(',', '.'))
sleep(1)
print('Contando cédulas', end='')
for c in range(0, 3):
    if c < 2:
        print('.', end='')
        sleep(1)
    else:
        print('.')
# print('Contando cédulas...')
print('-' * 30)
sleep(1)
print('Serão liberadas:')
total = valor
cédula = 50
totcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totcéd += 1

    else:
        if totcéd == 1:
            print(f'{totcéd} cédula de R$ {cédula}.')
        elif totcéd > 1:
            print(f'{totcéd} cédulas de R$ {cédula}.')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totcéd = 0
        if total == 0:
            break
print('-' * 30)
print('Confira seu dinheiro')
