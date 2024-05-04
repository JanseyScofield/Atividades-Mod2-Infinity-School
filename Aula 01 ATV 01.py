while True:
    try:
      idade = (int(input(f"Digite número: ")))
    except Exception:
        print("Número inválida! Digite novamente")
    else:
        if idade < 12:
            resp = "criança"
        elif idade >= 12 and idade <=17:
            resp = "adolescente"
        elif idade >=18 and idade <=59:
            resp = "adulto"
        else:
            resp = "idoso"
        print(f"Você é {resp}.")
    escolha = input("Quer digitar outra idade? Sim(s) ou Não(n)? ").lower()
    while escolha != 's' and escolha != 'n':
        escolha = input("Resposta inválida. Digite novamente: ").lower()
    if escolha == "n":
        break
    elif escolha == 's':
        continue

print("Fim!")
