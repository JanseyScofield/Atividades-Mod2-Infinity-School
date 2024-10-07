# Crie um dicionário com informações de produtos, incluindo nome, preço e quantidade em estoque. Implemente funções para adicionar, remover e atualizar produtos no 
# dicionário.

produtos = {
    "Nome" : [],
    "Preço" : [],
    "Quantidade em estoque" : [] 
}

def mostrar_produtos() -> None:
    '''Essa função mostra todos os produtos do dicionário. '''
    if len(produtos['Nome']) == 0:
        print("Não há produtos no estoque.")
    else:
        for chave, valor in produtos.items():
            print(f"{chave}: {valor}")

def adicionar_produto() -> None:
    '''Essa função adiciona um produto ao dicionário. '''
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
        except ValueError:
            print("Preço inválido.")
        else:
            break
    while True:
        try:
            quantidade_estoque = int(input("Digite a quantidade em estoque: "))
        except ValueError:
            print("Quantidade inválida.")
        else:
            break
        
    produtos["Nome"].append(nome)
    produtos["Preço"].append(preco)
    produtos["Quantidade em estoque"].append(quantidade_estoque)
    print("Produto adicionado com sucesso!")
    

def atualizar_estoque(nome : str, quantidade : int) -> None:
    '''Recebe o nome do produto e a quantidade que deve ser abatida do estoque.'''
    while True:
        try:
            operacao = int(input('''Deseja adicionar ao estoque (digite 1) ou remover (digite 2) do estoque?'''))
            if operacao != 1 and operacao != 2:
                raise ValueError
        except ValueError:
            print("Opcão inválida!")
        else:
            break
        
    indice = produtos["Nome"].index(nome)
    produtos['Quantidade em estoque'][indice] += -quantidade if operacao == 2 else quantidade
    print("Estoque atualizado com sucesso!")
    
def remover_produto() -> None:
    '''Essa função remove um produto do dicionário. '''
    nome = input("Digite o nome do produto que deseja remover: ")
    if nome in produtos["Nome"]:
        indice = produtos["nome"].index(nome)
        produtos['Nome'].pop(indice)
        produtos['Preço'].pop(indice)
        produtos['Quantidade em estoque'].pop(indice)
    else:
        print("O produto não existe no estoque!")
        
