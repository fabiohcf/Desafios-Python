def LeiaInt(msg):
    """
    Função para aceitar apenas  input de números inteiros.
    :param msg: input de número
    :return: número inteiro válido
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mNúmero não informado pelo usuário.\033[m')
            return 0
        else:
            return n


def LeiaFloat(msg):
    '''
    Função para aceitar apenas números reais validos.
    :param msg: input de número
    :return: número real válido
    '''
    while True:
        try:
            n = float(input(msg).replace(',','.'))
        except (TypeError, ValueError):
            print(f'\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não informou o npumero, foi atribuido "0".\033[m')
            return 0
        else:
            return n


