import json
import tarefas_model

def list():
    return

def create(nome : str, descricao : str, prioridade : str, categoria : str, status : str):
    nova_Tarefa = tarefas_model.Tarefa(nome, descricao, prioridade, categoria, status)
    salvar(nova_Tarefa)

def update():
    salvar()

def remove():
    salvar()


def salvar(tarefas):
    with open('repositorio_tarefas.json','w') as file:
        file.write(json.dump(tarefas, indent=4))
