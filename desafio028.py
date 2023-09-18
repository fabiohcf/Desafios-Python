from random import randint
from time import sleep


ncomp = randint(1, 6)
print('-'*60)
sleep(1)
print('Vamos jogar?')
sleep(1)
print('Escolhi um número entre 1 e 5, consegue adivinhar?')
sleep(2)
print('-'*60)
njog = int(input('Digite seu palpite: '))
print('Processando...')
sleep(2)
if njog == ncomp:
    print(f'O número que eu pensei foi {ncomp}')
    sleep(1)
    print('YOU WIN!')
else:
    print(f'O número que eu pensei foi {ncomp}')
    sleep(1)
    print('YOU LOSE!')
sleep(2)
