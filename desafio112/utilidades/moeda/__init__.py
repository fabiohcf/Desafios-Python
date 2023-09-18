def metade(n, formato=True):
    '''
    Calcula a metado do preço, retornando resultado com
    formatação (False) ou sem formatação (True).
    :param n: preço.
    :param formato: escolher formataçã: sim (False), não (True)
    :return: valor reajustaddo, com ou sem formatação.
    '''
    r = n / 2
    return r if formato == False else moeda(r)

def dobro(n, formato=True):
    '''
    Calcula o dobro do preço, retornando resultado com
    formatação (False) ou sem formatação (True).
    :param n: preço.
    :param formato: escolher formataçã: sim (False), não (True)
    :return: valor reajustaddo, com ou sem formatação.
    '''
    r = n * 2
    return r if formato == False else moeda(r)

def aumentar(n, taxa, formato=True):
    '''
    Calcula o preço aumentado em 'taxa'% , retornando resultado com
    formatação (False) ou sem formatação (True).
    :param n: preço.
    :param taxa: percentual de aumento do preço.
    :param formato: escolher formataçã: sim (False), não (True).
    :return: valor reajustaddo, com ou sem formatação.
    '''
    r = n + (n * taxa / 100)
    return r if formato == False else moeda(r)

def diminuir(n, taxa, formato=True):
    '''
    Calcula o preço reduzido em 'taxa'% , retornando resultado com
    formatação (False) ou sem formatação (True).
    :param n: preço.
    :param taxa: percentual de redução do preço.
    :param formato: escolher formataçã: sim (False), não (True).
    :return: valor reajustaddo, com ou sem formatação.
    '''
    r = n - (n * taxa / 100)
    return r if formato == False else moeda(r)

def moeda (preço=0, moeda='R$ '):
    '''
    Formata valores para modelo monetário.
    :param preço: preço.
    :param moeda: cifrão.
    :return: valor em formato monetário.
    '''
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(p,ta=10, tr=5):
    from desafio110 import moeda
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda.moeda(p)}')
    print(f'Metade do preço: \t{moeda.metade(p)}')
    print(f'Dobro do preço: \t{moeda.dobro(p)}')
    print(f'{ta} % de aumento: \t{moeda.aumentar(p, ta)}')
    print(f'{tr} % de redução: \t{moeda.diminuir(p, tr)}')
    print('-' * 30)



