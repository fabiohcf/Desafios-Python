# calculadora de IMC
# input de peso e altura e calcule o IMC
# < 18.5 - baixo peso
# 18.5 < imc < 25 - peso ideal
# 25 < imc < 30 - sobrepeso
# 30 < imc < 40 - obesidade
# > 40 - obesidade mórbida
print('-=-'*10)
print(f'{"Calculadora de IMC":^30}')
print('-=-'*10)
peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura**2)
print(f'Seu IMC é {imc:.1f}.')
print('Sua classificação é ', end='')
if imc < 18.5:
    print('BAIXO PESO.')
elif 18.5 <= imc < 25:
    print('PESO IDEAL.')
elif 25 <= imc < 30:
    print('SOBREPESO.')
elif 30 <= imc < 40:
    print('OBESIDADE.')
elif imc >= 40:
    print('OBESIDADE MORBIDA.')
