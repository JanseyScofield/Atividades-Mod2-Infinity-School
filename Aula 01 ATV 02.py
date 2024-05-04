#Faça um programa que leia 3 números e informe o maior número e o menor.

num = []
maior = 0
menor = 0
for i in range (3):
    num.append(int(input(f"Digite número {i+1}: ")))
    if i == 0:
        maior = num[i]
        menor = num[i]
    else:
        if num[i] >= maior:
            maior = num[i]
        elif num[i] <= menor:
            menor = num[i]
print(f"O maior é {maior} e o menor é {menor}.")
