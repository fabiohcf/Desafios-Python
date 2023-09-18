print(f'{"Calculadora de Média":=^50}')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('-' * 50)
media = (n1 + n2) / 2
print(f'Sua nota média é {media:.2f}')
if media < 5:
    print('Situação: Reprovado!')
elif 5 <= media < 7:
    print('Situação: Recuperação!')
elif media >= 7:
    print('Situação: Aprovado!')
    print('Parabéns.')
