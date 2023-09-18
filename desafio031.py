# input distância da viagem (Km)
# calcular preço da passagem:
#   * R$ 0,50 / Km (Viagens até 200 Km)
#   * R$ 0,45 / km (Viagens acima de 200 Km)

distancia = float(input('Qual a distância da viagem (Km)?\n     '))
valor = 0
if distancia <= 200:
    valor = distancia * 0.5
elif distancia > 200:
    valor = distancia * 0.45
print(f'O valor da sua passagem é R$ {valor:.2f}' .replace(',', '.'))
