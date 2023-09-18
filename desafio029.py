# input de dado de velocidade
# <= 80:  tenha um bom dia, dirija com segurança
# > 80: Multa! R$ 7,00 / Km excedido

vel = float(input('Qual velocidade do veículo?'))
if vel > 80:
    print('Multa! Você excedeu o limite de velocidade de 80Km/h.')
    print(f'Você deve pagar uma multa de R$ {(vel - 80) * 7:.2f}')
print('Tenha um bom dia, dirija com segurança!')
