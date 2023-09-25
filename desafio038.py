# input de dois números inteiros
# mostrar o maior valor ou dizer se são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'{n1} é o maior valor.')
elif n2 > n1:
    print(f'{n2} é o maior valor.')
else:
    print(f'Os números digitados têm o mesmo valor.')