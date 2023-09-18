def metade(n, formato=True):
    r = n / 2
    return r if formato == False else moeda(r)

def dobro(n, formato=True):
    r = n * 2
    return r if formato == False else moeda(r)

def aumentar(n, taxa, formato=True):
    r = n + (n * taxa / 100)
    return r if formato == False else moeda(r)

def diminuir(n, taxa, formato=True):
    r = n - (n * taxa / 100)
    return r if formato == False else moeda(r)

def moeda (preço=0, moeda='R$ '):
    return f'{moeda}{preço:.2f}'.replace('.',',')





