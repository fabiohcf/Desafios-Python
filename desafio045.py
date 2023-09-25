# jokenpo

from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
njog = int(input('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Qual sua escolha? '''))
if njog > 2:
    print('Jogada inválida.')
    exit()
njog -= 1
ncomp = randint(1, 3)
ncomp -= 1
sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(1)
print(f'Você escolheu {lista[njog]}\nO computador escolheu {lista[ncomp]}')
sleep(1)

if njog == ncomp:
    print('Vocês EMPATARAM!')
elif njog == 0:
    if ncomp == 1:
        print('Vocẽ PERDEU!')
    elif ncomp == 2:
        print('Vocẽ VENCEU!')
elif njog == 1:
    if ncomp == 2:
        print('Vocẽ PERDEU!')
    elif ncomp == 0:
        print('Vocẽ VENCEU!')
elif njog == 2:
    if ncomp == 0:
        print('Vocẽ PERDEU!')
    elif ncomp == 1:
        print('Vocẽ VENCEU!')
sleep(1)
