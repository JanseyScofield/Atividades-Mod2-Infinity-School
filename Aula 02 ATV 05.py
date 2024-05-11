# Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

teams = []
soma = 0

somaTime = 0

while True:
    equipeNome = input("Digite o nome da equipe: ")
    pontuacoes = []
    for iCont in range(3):
        while True:
            try:
                pontuacoes.append(int(input(f"Digite a pontuação da {iCont + 1}° prova: ")))
            except Exception:
              print("Valor inválido. Digite novamente.")
            else:
                break
    somaTime = sum(pontuacoes)
    mediaTime = somaTime/3 
    tuplaTime = (equipeNome, pontuacoes, mediaTime)
    teams.append(tuplaTime)
    escolha = input("Deseja continuar adiconando outra equipe? Sim(s) ou Não(n)? ").lower()
    while escolha != 's' and escolha != 'n':
        escolha = input("Valor inválido. Digite novamente: ").lower()
    if escolha == 'n':
        break
teams.sort(reverse = True)
print(teams)

classificacao = []

for iCont in range (len(teams)):
    time = teams[iCont][0]
    media = teams[iCont][2]
    tuplaClass = (time, media)
    classificacao.append(tuplaClass)

classificacao.sort(key = lambda x: x[1], reverse=True)

for i in range(len(classificacao)):
    print(f"{i + 1}° - {classificacao[i]}")
  
