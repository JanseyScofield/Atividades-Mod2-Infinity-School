# Crie uma função que aceita uma lista de números e use a função map para retornar uma nova lista contendo o dobro de cada número na 
# lista de entrada.

lista = [3, 12, 31, 78] 
dobrar_num = list(map(lambda x : x*2, lista))

print(dobrar_num)
