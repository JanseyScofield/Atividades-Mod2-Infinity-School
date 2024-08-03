from Biblioteca import Biblioteca
from Livro import Livro
from Usuario import Usuario

class Emprestimo:
    def __init__(self):
        self.__usuario
        self.__livro
        self.__biblioteca 

    def procurar_livro(self, livro: Livro, biblioteca: Biblioteca):
        if livro not in biblioteca.lista_livros:
            return False
        return True

    def procurar_usuario(self, usuario):
        if 

    def criar_emprestimo(self):
        pass