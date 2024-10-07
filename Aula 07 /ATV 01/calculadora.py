from functools import reduce

def  receber_num(posiçao_num : int) -> float:
    """Faz o tratamento dos números inseridos."""
    while True:
        try:
            num = float(input(f"Digite o {posiçao_num}° número: "))
        except Exception:
            print("Valor inválido. Digite novamente:")
        else:
            return num

def somar( num : float, outros_num : list) -> float:
    """Recebe pelo menos dois números e retorna a soma deles"""
    soma = num
    soma += sum(outros_num)
    return soma

def subtrair( num : float, outros_num : list) -> float:
    """Recebe pelo menos dois números e retorna a subtração de todos eles"""
    subtracao = num
    subtracao -= sum(outros_num)
    return subtracao

def dividir( num : float, outros_num : list) -> float:
    """Recebe pleo menos dois números e retorna o quociente da divisão de todos eles."""
    tem_0 = False
    for numero in outros_num:
        if numero == 0:
            tem_0 = True
            break
    if num == 0 or tem_0:
        return 'Divisões por 0 dão resultado indeterminados'
    divisao = num
    divisao /= reduce(lambda x,y: x/y, outros_num)
    return divisao

def multiplicar( num : float, outros_num : list) -> float:
    """Recebe pelo menos dois números e retorna o produto de todos eles"""
    multiplicacao = num
    multiplicacao *= reduce(lambda x,y: x*y, outros_num)
    return multiplicacao