# Faça um programa que peça 10 números inteiros,calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = []
pares = 0
impares = 0

for iCont in range(10):
    while True:
        try: 
            num.append(int(input(f"Digite o {iCont + 1}° número: ")))
        except Exception:
            print("Digite um valor válido.")
        else:
            break
    if num[iCont] % 2 == 0:
        pares += 1
    else:
        impares += 1
    
print(f"Número de pares: {pares}.\nNúmeros de ímpares: {impares}.")
