# input de dois valores. somar, multiplicar, maior valor, novo input, sair

from time import sleep
print('Informe dois valores:')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    sleep(1)
    print(f'{"MENU":-^26}')
    print('''[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Digitar novos números
[5] Sair    ''')
    print('-'*26)
    resp = int(input('Digite sua opção: '))

    if resp == 1:
        sleep(1)
        print(f'{n1} + {n2} = {n1 + n2}.')
    elif resp == 2:
        sleep(1)
        print(f'{n1} x {n2} = {n1 * n2}.')
    elif resp == 3:
        sleep(1)
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print('Os valores são iguais.')
    elif resp == 4:
        print('Informe novos valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif resp == 5:
        print('Saindo do programa...')
        sleep(2)
        break
    else:
        print('opção inválida.')