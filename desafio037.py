# input de número inteiro e usuário escolher base de conversão:
# 1 - binário
# 2 - octal
# 3 - hexadecimal


print('-=-'* 10)
print(f'{"Conversão de números":^30}')
print('-=-'* 10)
num = int(input('Digite um número inteiro: '))
base = int(input('''
Escolha a base para conversão:
[ 1 ] - binário
[ 2 ] - octal
[ 3 ] - hexadecimal
opção: '''))

if base == 1:
    print(f'{num} em base binária é {bin(num)}')
elif base == 2:
    print(f'{num} em base octal é {oct(num)}')
elif base == 3:
    print(f'{num} em base hexadecimal é {hex(num)}')
else:
    print('Número inválido, tente novamente.')
