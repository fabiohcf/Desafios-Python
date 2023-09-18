# ler um número e informar se é par ou ímpar

num = int(input('Digite um número para descobir se ele é par ou ímpar: '))
if num % 2 == 0:
    print(f'{num} é um número par.')
else:
    print(f'{num} é um número ímpar.')
