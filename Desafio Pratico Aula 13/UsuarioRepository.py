class UsuarioRepository:
    def __init__(self):
        self.__lista_usuario = []
    

    def adicionar_usuario(self, usuario):
        try: 
            self.__lista_usuario.append(usuario)
        except:
            print("Falha ao cadastrar. Confira os dados e tente novamente.")
        else:
            print(f"{usuario.nome} foi adicioando com sucesso!")
    
    def listar_usuarios(self):
        for usuario in self.__lista_usuario:
            print(f"Nome: {usuario.nome}. Id: {usuario.id}")
        print("-------------------------------------------")

    def apagar_usuario(self, usuario):
        try:
            ndx_usuario = self.__lista_usuario.index(usuario)
            self.__lista_usuario.pop(ndx_usuario)
        except:
            print("Falha ao remover. Verifique os dados e tente novamente.")
        else:
            print(f"{usuario.nome} foi removido com sucesso!")

    def editar_usuario_por_id(self, id):
        try:
            for usuario in self.__lista_usuario:
                if usuario.id == id:
                    usuario.nome = ("Qual o nove nome do usuario? ")
        except:
            print("Falha ao alterar. Verifique os dados e tente novamente.")
        else:
            print("Nome alterado com sucesso!")