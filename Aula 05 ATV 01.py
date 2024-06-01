# Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função. A função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.

def calcular_media(n1 : float, n2 : float, n3 : float) -> float:
    """Recebe 3 notas e retorna uma média."""
    return (n1 + n2 + n3) / 3

notas = []

for iCont in range(3):
    notas.append(float(input(f"Digite a {iCont + 1}ª nota: ")))

print(f"A média ficou: {calcular_media(notas[0], notas[1], notas[2])}")
