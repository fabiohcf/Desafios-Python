from datetime import date

print(f'{"Confederação Nacional de Natação":=^50}')
anonasc = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
print(f'O atleta tem {idade} anos')
if idade < 9:
    print('Categoria: MIRIM')
elif 9 <= idade < 14:
    print('Categoria: INFANTIL')
elif 14 <= idade < 19:
    print('Categoria: JÚNIOR')
elif 19 <= idade < 25:
    print('Categoria: SÊNIOR')
elif idade >= 25:
    print('Categoria: MASTER')

