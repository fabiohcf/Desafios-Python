# mostre a tabuada de um número solicitado pelo usuário


print(f'{"TABUADA":-^52}')
num = int(input('Digite um número para visualizar sua tabuada: '))
print('-'*12)
print(f'TABUADA DE {num}')
print('-'*12)
for c in range(1,11):
    print(f'{num} x {c:<2} = {num*c:<2}')
print('-'*12)

