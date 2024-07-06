import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#333'
    def botao_cadastrar(e):
      page.title = ft.Text("USUÁRIO CADASTRADO!").value
      page.update()

    nome = ft.TextField(label="Nome:", width = 500, bgcolor='#efefef')
    email = ft.TextField(label="E-mail:", width = 500, bgcolor='#efefef')
    senha = ft.TextField(label="Senha:", width = 500, bgcolor='#efefef')
    
    coluna = ft.Column(
       controls=[nome,
                 email, 
                 senha, 
                 ft.ElevatedButton(text="Cadastrar", on_click=botao_cadastrar, bgcolor='#efefef')],
       alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(coluna)

ft.app(target=main)
