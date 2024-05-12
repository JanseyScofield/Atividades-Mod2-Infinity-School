# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
#Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e 
#ímpares, respectivamente.

numbers = []

for iCont in range(10):
    numbers.append(int(input(f"Digite o {iCont + 1}° número: ")))

par = []
impar = []

for item in numbers:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)

print(f"Os números pares são: {par}")
print(f"Os números ímpares são: {impar}")

tupla = ((f"Quantidade de pares: {len(par)}", f"Soma pares: {sum(par)}"), (f"Quantidade ímpares: {len(impar)}", f"Soma ímpares: {sum(impar)}"))
print(tupla)
