# input ano de nascimento
# < 18 (calcular tempo para o alistamento)
# = 18 (Hora de se apresentar)
# > 18 ( calcular tempo que deveria ter se alistado)


from datetime import date
print('-=-'*15)
print(f'{"Serviço de alistaento militar":^45}')
print('-=-'*15)
anonasc = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade < 18:
    print(f'Você tem {idade} anos, em {18 - idade} ano(s) devererá se alistar nas forças armadas')
elif idade == 18:
    print(f'Você tem {idade} anos, procure as forças armadas para se alistar.')
elif idade > 18:
    print(f'Vocẽ tem {idade} anos, deveria ter se alistado há {idade  - 18} ano(s), procure as forças armadas para regularizar sua situação.')
