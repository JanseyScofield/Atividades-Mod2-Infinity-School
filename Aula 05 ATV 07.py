# Crie uma função chamada criar_lista_de_compras que aceita um número variável de itens de compras como
# argumentos posicionais (usando *args). A função deve criar e retornar uma lista de compras que contenha todos os itens fornecidos.

def criar_lista_de_compras(*itens : str) -> list:
    listaDeCompras = []
    for item in itens:
        listaDeCompras.append(item)
    return listaDeCompras

print(criar_lista_de_compras("pão", "manteiga", "faca"))
