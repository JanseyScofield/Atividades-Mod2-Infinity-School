import services

def list():
    return

def create():
    while True:
        nome = input("Digite o nome da tarefa: ")
        if nome:
            break
        else:
            print("O campo 'nome' é obrigatório!")
    descricao = input("Digite a descrição da tarefa: ")
    while True:
        prioridade = input("Qual é a prioridade? ")
        if prioridade:
            break
        else:
            print("O campo 'prioridade' é obrigatório!")
    while True:
        categoria = input("Digite a categoria: ")
        if nome:
            break
        else:
            print("O campo 'categoria' é obrigatório!")
    while True:
        status = input("Digite o status: ")
        if nome:
            break
        else:
            print("O campo 'status' é obrigatório!")

    services.create(nome, descricao, prioridade, categoria, status)

def update():
    return

def remove():
    return