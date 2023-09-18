def LeiaInt(msg):
    '''
    Função que apenas aceita entrada de números inteiros válidos.
    :param msg: input de número inteiro
    :return: caso número inteiro válido, retorna valor
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO, digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


#programa principal
n = LeiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')
