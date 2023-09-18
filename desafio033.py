# input de 3 números e mostrar qual o maior e menor
lista = []
'''
for c in range (0,3):
    (num:=int(input(f'Digite o {c+1}º número: ')))
    lista.append(num)
lista = sorted(lista)
print(f'O menor número digitado foi {lista[0]}.')
print(f'O maior número digitado foi {lista[2]}.')
'''
nmenor = nmaior = 0
for c in range(0, 3):
    num = int(input(f'Digite o {c+1}º número: '))
    if c == 0:
        nmenor = nmaior = num
    else:
        if num > nmaior:
            nmaior = num
        elif num < nmenor:
            nmenor = num
print(f'O menor número digitado foi {nmenor}.')
print(f'O maior número digitado foi {nmaior}.')
