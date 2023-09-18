from time import sleep


print(f'{"CALCULADORA DE EMPRÉSTIMO":-^40}')
sleep(1)
valor = float(input('Qual o valor do imóvel?\nR$ '))
sal = float(input('Qual sua renda mensal?\nR$ '))
tempo = int(input(f'Qual o tempo do financiamento? (meses)\n'))
limite = sal*30/100
prest = valor/tempo
sleep(1)
if prest > limite:
    print('Empréstimo negado!')
    sleep(1)
    print('O valor da prestação excedeu o limite de 30% do seu salário.')
    sleep(1)
    tmin = valor/limite
    print(f'O tempo mínimo de finanaciamento deste imóvel, compatível com sua renda, é de {tmin:.0f} meses.')

else:
    print('Parabéns!')
    sleep(1)
    print('Empréstimo aprovado.')
    print(f'Serão {tempo} parcelas de R$ {prest:.2f}.')