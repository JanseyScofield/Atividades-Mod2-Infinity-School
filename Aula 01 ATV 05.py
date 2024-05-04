# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

maior = 0
menor = 0
soma = 0

qtdVezes = int(input("Quantos número você deseja digitar? "))
for iCont in range(qtdVezes):
    while True:
        try:
            num = float(input(f"Digite o {iCont + 1}° número: "))
        except Exception:
            print("Valor inválido. Digite novamente: ")
        else:
            break
    soma += num
    if iCont == 0:
        maior = num
        menor = num
    else:
        if num >= maior:
            maior = num
        elif num <= menor:
            menor = num
print(f"O maior número foi {maior}. O menor número foi {menor}. A soma entre eles resultou em {soma}.")
