# Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

emailCadastrado = input("Cadastre um email: ")
senhaCadastrada =  input("Crie uma senha: ")

while True:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        if  email != emailCadastrado or senha != senhaCadastrada:
            print("Email ou senha incorretos. Digite novamente:")
        else:
            break

print("Email e senha corretos!")