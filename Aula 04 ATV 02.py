# Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa noite!"conforme o horário.

def saudadacaoPeriodo(horario : int):
    """Recebe um horário e imprime uma saudação referente."""

    if horario < 0 or horario > 24:
        print("Horário inválido!")
    else:
        if horario >= 5 and horario <= 12:
            print("Bom dia!")
        elif horario >=13 and horario <=17:
            print("Boa tarde!")
        else:
            print("Boa noite!")

saudadacaoPeriodo(29)
