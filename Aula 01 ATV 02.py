#Faça um programa que leia 3 números e informe o maior número e o menor.
while True:
    num = []
    maior = 0
    menor = 0   
    for i in range (3):
        while True:
            try:
                num.append(int(input(f"Digite número {i+1}: ")))
            except Exception:
                print("Número inválido! Digite novamente")
            else:
                if i == 0:
                    maior = num[i]
                    menor = num[i]
                else:
                    if num[i] >= maior:
                        maior = num[i]
                    elif num[i] <= menor:
                        menor = num[i]
                break
    print(f"O maior é {maior} e o menor é {menor}.")
    escolha = input("Quer digitar outra sequência? Sim(s) ou Não(n)? ").lower()
    num.clear()
    while escolha != 's' and escolha != 'n':
        escolha = input("Resposta inválida. Digite novamente: ").lower()
    if escolha == "n":
        break
    elif escolha == 's':
        continue


         
