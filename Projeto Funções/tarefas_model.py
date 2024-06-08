class Tarefa:
    def __init__(self, nome : str, descricao : str, prioridade : str, categoria : str, status : str):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.status = status
    def get(self):
        print(f"NOME : {self.nome}")
        print(f"DESCRIÇÃO : {self.descricao}")
        print(f"PRIORIDADE : {self.prioridade}")
        print(f"CATEGORIA : {self.categoria}")
        print(f"STATUS : {self.status}")