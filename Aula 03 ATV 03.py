# Crie um programa que recebe dois conjuntos e exibe a interseção deles.

conjunto1 = set()

qtdVezes = int(input("Quantos itens precisa adicionar no primeiro conjunto? "))

for iCont in range(qtdVezes):
    item = input(f"Digite o item {iCont + 1}: ")
    conjunto1.add(item)

conjunto2 = set()

qtdVezes2 = int(input("Quantos itens precisa adicionar no segundo conjunto? "))

for iCont in range(qtdVezes):
    item = input(f"Digite o item {iCont + 1}: ")
    conjunto2.add(item)

conjunto3 = conjunto1&conjunto2

print(conjunto3)
