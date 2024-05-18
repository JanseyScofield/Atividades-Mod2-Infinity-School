frutas = set()

frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

print(frutas)

banana = False
for item in frutas:
    if(item == "banana"):
        banana = True

if banana == True:
    print("Tem banana")
else:
    print("Não tem banana")

frutas_vermelhas = set()

frutas_vermelhas.add("morango")
frutas_vermelhas.add("cereja")
frutas_vermelhas.add("framboesa")

print(frutas_vermelhas)
