# soma dos números ímpares, múltiplos de três, no intervalo entre 1, 500

s = 0
lista = []

for c in range(1,501):
    if c%2 == 1:
        if c%3 == 0:
            lista.append(c)
            s += c
print(f'a soma de {lista} é {s}.'.replace('[','(').replace(']',')').replace(',',' +'))
