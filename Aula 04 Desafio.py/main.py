import funcoesCalc

while True:
    print("---------Calculadora---------")
    while True:
        try: 
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except Exception:
            print("Valores inválidos. Digite novamente.")
        else:
            break
    operacao = input(""" 
            Digite a operação que deseja realizar:
                + : adição;
                - : subtração;
                ÷ : divisão;
                x : multiplicação;
                S : Sair.
        """).upper()
    
    match operacao:
        case '+':
            print(f"{n1} + {n2} = {funcoesCalc.somar(n1,n2)}")
        case '-':
            print(f"{n1} - {n2} = {funcoesCalc.subtrair(n1,n2)}")
        case "÷" : 
            print(f"{n1} ÷ {n2} = {funcoesCalc.dividir(n1,n2)}")
        case 'X':
            print(f"{n1} x {n2} = {funcoesCalc.multiplicarr(n1,n2)}")
        case 'S':
            print("Saindo...")
            break
        case _:
            print("Valor inválido. Digite novamente.")     
