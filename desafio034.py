# input de salário
#   > de R$1250,00 reajuste de 10%
#   <= R$1250,00 reajuste de 15%
print('-'*40)
print(f'{"Calculadora de reajuste salarial":^40}')
print('-'*40)
sal = float(input('Informe seu salário: R$ '))
if sal > 1250:
    novosal = sal + (sal * 0.10)
else:
    novosal = sal + (sal * 0.15)
print(f'Seu novo salário será R% {novosal:.2f}'. replace('.', ','))
