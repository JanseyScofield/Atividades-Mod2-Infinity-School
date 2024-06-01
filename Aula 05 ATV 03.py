# Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos posicionais (usando *args). 
# A função deve concatenar todas as strings em uma única string e retorná-la.

def concatenar_strings(*strings):
    return ''.join(strings)

print(concatenar_strings("a","b","c","d"))
