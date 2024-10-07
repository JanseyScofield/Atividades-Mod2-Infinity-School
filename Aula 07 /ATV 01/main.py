import calculadora as calc

operacao = {
    "1" : calc.somar,
    "2" : calc.subtrair,
    "3" : calc.multiplicar,
    "4" : calc.dividir,
}


print("Bem vindo(a) a calculadora!")
while True:
    numeros = []
    num1 = 0
    iCont = 1
    lista_escolhas = ["1", "2", "3", "4", "5"]
    print("""Operações
      1 - Soma
      2 - Subtração
      3 - Multiplicação
      4 - Divisão
      5 - Sair""")
    while True:
        try:
            escolha = input("Digite a operação desejada: ")
            if escolha not in lista_escolhas:
                ValueError
        except:
            print("Valor inválido. Digite novamente.")
        else:
            if escolha == '5':
                exit()
            break
    while True:       
        if iCont == 1:
            num1 = calc.receber_num(iCont)
        else:
            numeros.append(calc.receber_num(iCont))
        iCont += 1
        if iCont >= 3:
            escolha_qtd_numeros = input("Deseja digitar outro número? Digite 'N' para sair: ").upper()
            if escolha_qtd_numeros == "N":
                break
    resultado = operacao[escolha](num1, numeros)
    print(f"O resultado da operação foi : {resultado}.")

print("Obrigado! Volte sempre!")