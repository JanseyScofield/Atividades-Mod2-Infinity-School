from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.__lista_livros = []

    def adicionar_livro(self, titulo, autor):
        try:
            novo_livro = Livro(titulo, autor)
        except:
            print(f"Não foi possível adicionar {titulo} de {autor}. Verifique os dados passados.")
        else:
            self.__lista_livros.append(novo_livro)
            print(f"{titulo} de {autor} foi adicionado a biblioteca com sucesso!")
        
    def remover_livro(self, titulo):
       try:
        ndx_livro = self.__lista_livros.index(titulo)
        self.__lista_livros.pop(ndx_livro)
       except:
           print(f"Não foi possível remover {titulo}. Verifique o nome digitado.")
       else:
           print(f"{titulo} foi removido da biblioteca com sucesso!")

    @property
    def lista_livros(self):
        return self.__lista_livros