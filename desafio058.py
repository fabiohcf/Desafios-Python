# melhore o desafio028, tentar adivinhar um número entre 1 e 10, ate acertar e contar o npumero de tetativas usadas

from random import randint
from time import sleep

ncomp = randint(1,11)
print('-'*60)
sleep(1)
print('Vamos jogar?')
sleep(1)
print('Escolhi um número entre 1 e 10, consegue adivinhar?')
sleep(1)
print('-'*60)

t = 0
while True:
    njog = int(input('Digite seu palpite: '))
    t += 1
    print('Processando...')
    sleep(1)
    if njog == ncomp:
        print(f'Eu pensei exatamento no número {ncomp}, você conseguiu adivinhar na {t}ª tentativa. Parabéns.')
        sleep(1)
        print('YOU WIN!')
        break
    else:
        if njog < ncomp:
            print(f'Errou, pensei em um número maior.\nTente novamente.')
        else:
            print(f'Errou, pensei em um número menor.\nTente novamente.')
        sleep(1)
sleep(2)


