print(f'{" Analisador de triâgulos ":=^40}')
print('Informe os segmentos de reta e verifique se eles podem formar um triângulo:')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
x = sorted([s1, s2, s3])

if (x[0] + x[1]) > x[2]:
    print(f'Os segmentos de reta {s1, s2, s3} \033[36mPODEM\033[m formar um triâgulo.')
else:
    print(f'Os segmentos de reta {s1, s2, s3} \033[31mNÃO PODEM\033[m formar um triângulo.')
