# Faça um programa que peça para n  pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem  adulta ou idosa, conforme a média calculada.

soma = 0
qtd = 0
while True:
    while True:
        try:
            idade = int(input("Digite uma idade: "))
        except Exception:
            print("Idade inválida! Digite novamente.")
        else:
            break
    soma += idade
    qtd += 1
    escolha = input("Deseja continuar? Sim(s) ou Não(n)? ").lower()
    while escolha != 's' and escolha != 'n':
        escolha = input("Resposta inválida. Digite novamente: ").lower()
    if escolha == 'n':
        break
        
media = soma/qtd

if media <= 25:
    print("Jovem.")
elif media >=26 and media <= 60:
    print("Adulto.")
else:
    ("Idoso.")
