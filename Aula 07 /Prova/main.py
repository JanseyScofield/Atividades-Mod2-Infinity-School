# Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.
import random

def lancar_dados() -> int:
    primeiro_dado = random.randint(1,6)
    segundo_dado = random.randint(1,6)
    return primeiro_dado + segundo_dado

print(lancar_dados())
