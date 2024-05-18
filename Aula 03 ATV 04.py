# Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações separadamente.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

dados = {
    "nome" : nome,
    "idade" : idade
}

print(dados)

for chave , valor in dados.items():
    print(f"{chave} : {valor}")
