from desafio115.lib.interface import *
from time import sleep
from desafio115.lib.arquivo import *


arquivo = 'pessoas.txt'
if not existeArq(arquivo):
    criarArq(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        leiaArq(arquivo)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mERRO! Digite um valor válido\033[m')
    sleep(2)
