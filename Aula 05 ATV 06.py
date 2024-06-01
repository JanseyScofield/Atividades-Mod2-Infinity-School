# Crie uma função que aceita uma lista de strings e encontre a maior string na lista.

def encontrar_maior_string(lista : list):
    maior_string = lista[0]
    for string in lista:
        if len(string) > len(maior_string):
            maior_string = string
    return maior_string

listaString = ["oi", "tudo bem?", "olá"]
print(encontrar_maior_string(listaString))
