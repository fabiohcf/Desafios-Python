def metade(n):
    return n/2

def dobro(n):
    return n*2

def aumentar(n, taxa):
    return n + (n * taxa/100)

def diminuir(n, taxa):
    return n - (n * taxa/100)

def moeda (preço=0, moeda='R$ '):
    return f'{moeda}{preço:.2f}'.replace('.',',')





