# Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos, comprimento e largura de um retângulo, 
# e retorna a área desse retângulo. Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura e imprimir 
# a área calculada.

def calcular_area_retangulo(comprimento : float, largura : float) -> float:
    """Recebe dois argumentos, comprimento e largura de um retângulo, e retorna a área desse retângulo."""
    return comprimento * largura

while True:
    try:
        comprimento = float(input("Digite o comprimento do retângulo em metros quadrados: "))
    except:
        print("Comprimento inválido. Digite novamente.")
    else:
        break

while True:
    try:
        largura = float(input("Digite o comprimento do retângulo em metros quadrados: "))
    except:
        print("Largura inválida. Digite novamente.")
    else:
        break

areaRetangulo = calcular_area_retangulo(comprimento, largura)
print(f"A área do trinâgulo é {areaRetangulo} m².")
