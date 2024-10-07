import produtos

menu = {
    1 : produtos.mostrar_produtos,
    2 : produtos.adicionar_produto,
    3 : produtos.atualizar_estoque,
    4 : produtos.remover_produto,
    5 : exit
}

while True:
    print("-------------------Produtos-------------------")
    print("""
    1 - Mostrar produtos
    2 - Adicionar produtos
    3 - Atualizar estoque
    4 - Remover produtos
    5 - Sair
    """)
    while True:
        try:
            opcao = int(input("Digite uma opção acima: "))
            if opcao not in menu:
                raise ValueError
        except ValueError:
            print("Digite uma opção válida!")
        else:
            break
    menu[opcao]()
