def contar_palavras(texto : str) -> str:
   """Essa função recebe um texto e retorna a quantidade de palavras."""

   listaTexto = texto.split(" ")
   return f'A quantidade de palavras desse texto é igual a: {len(listaTexto)}.'

def contar_letras(texto : str) -> str:
   """Essa função recebe um texto e retorna a quantidade de palavras."""

   qtdLetras = list(filter(lambda x: x != " ", texto))
   return f'A quantidade de letras desse texto é igual a: {len(qtdLetras)}.'

def inverter_o_texto(texto : str) -> str:
   """Essa função recebe um texto e retorna ele invertido."""
   
   listaTexto = texto.split(" ")
   qtdPalavras = len(listaTexto)
   novaPalavra = ''
   
   while qtdPalavras > 0:
      if qtdPalavras == 1:
         novaPalavra += listaTexto[0]
      else:
         novaPalavra += listaTexto[qtdPalavras - 1] + " "
      qtdPalavras -= 1
   return f'O texto invertido é : {novaPalavra}.'

def substituir_palavra(texto : str, palavraAntiga : str, palavraNova : str) -> str:
   """Essa função recebe um texto, a palavra que vai ser substituída e a palavra nova e retorna o texto com a palavra substuida."""

   listaTexto = texto.split(" ")
   palavrasNovoTexto  = list(map(lambda x: palavraNova if x == palavraAntiga else x, listaTexto ))
   novoTexto = ''
   for palavra in palavrasNovoTexto:
      if palavrasNovoTexto[len(palavrasNovoTexto) -1]  == palavra:
         novoTexto += palavra
      else:
         novoTexto += palavra + ' '

   return f'O novo texto é: {novoTexto}.'

def processador_texto(texto : str, **operacoes : dict) -> str:
   """Essa função recebe um texto e pode fazer 4 operações com ele: contar as letras, contar as palavras, inverter o texto e substituir palavras antigas por novas. Ao fim,retorna um resultado personalizado."""

   resultado = ''   
   for chave,valor in operacoes.items():
      match chave, valor:
         case operacao, 'contar_palavras':
           resultado += contar_palavras(texto)
         case operacao, 'contar_letras':
            resultado  +=  contar_palavras(texto)
         case operacao, 'inverter_o_texto':
            resultado += inverter_o_texto(texto)
         case operacao, 'substuir_palavra':
            antigaPalavra = ''
            novaPalavra = ''
            for chave, valor in operacoes.items():
               if chave ==  'palavra_antiga':
                  antigaPalavra = valor
               if chave == 'palavra_nova':
                  novaPalavra = valor                  
            resultado += substituir_palavra(texto, antigaPalavra, novaPalavra)

      return resultado

print(processador_texto('Tudo bem', operacao = 'contar_palavras', operacao = 'contar_letras'))