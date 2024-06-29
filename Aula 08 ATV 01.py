# Dada uma lista de números, crie uma nova lista contendo apenas os números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x :x % 2 == 0, lista))

print(pares)
