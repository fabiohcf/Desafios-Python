print(f'{" Analisador de triâgulos ":=^40}')
print('Informe os segmentos de reta e verifique se eles podem formar um triângulo:')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
x = sorted([s1, s2, s3])

if (x[0] + x[1]) > x[2]:
    print(f'Os segmentos de reta {s1, s2, s3} \033[36mPODEM\033[m formar um triâgulo ', end='')
    if s1 == s2 == s3:
        print('\033[36mretângulo\033[m.')
    elif s1 != s2 != s3:
        print('\033[36mescaleno.\033[m')
    else:
        print('\033[36misóceles.\033[m')

else:
    print(f'Os segmentos de reta {s1, s2, s3} \033[31mNÃO PODEM\033[m formar um triângulo.')
