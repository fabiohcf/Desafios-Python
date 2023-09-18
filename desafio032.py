# input de um ano para descobrir se é um ano bissexto
from datetime import date

print(f'\n{"="*5} Descubra se um ano é bissexto {"="*5}\n')
ano = int(input('Informe uma ano para ser analisado: \n(Digite 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} \033[32mé\033[m um ano bissexto.')
else:
    print(f'{ano} \033[31mNÃO\033[m é um ano bissexto.')
