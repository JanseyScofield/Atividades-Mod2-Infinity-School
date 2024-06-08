import json
import tarefas_model

repositorio_tarefas = []

def list_():
    return repositorio_tarefas

def create(nome : str, descricao : str, prioridade : str, categoria : str, status : str):
    nova_tarefa = tarefas_model.Tarefa(nome, descricao, prioridade, categoria, status)   
    repositorio_tarefas.append(nova_tarefa)
def update():
    salvar()

def remove():
    salvar()


def salvar(tarefas):
    with open('repositorio_tarefas.json','w') as file:
        file.write(json.dumps(tarefas, indent=4))
