class Usuario:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id