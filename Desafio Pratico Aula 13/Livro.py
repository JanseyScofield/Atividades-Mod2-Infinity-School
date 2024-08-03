class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

        @property
        def titulo(self):
            return self.__titulo
        
        @property
        def autor(self):
            return self.__autor

