# Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo apenas os números pares 
# da lista de entrada.

lista = [1, 2, 3, 4,5, 6, 7, 8, 9]

def retornar_pares(numero : int) -> int:
    """Retorna apenas os números pares da lista"""
    if numero % 2 == 0:
        return numero

print(list(filter(retornar_pares, lista)))
