# Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

dicionario_produtos  = {}

for iCont in range(0, 5):
    produto = input(f"Digite o nome do produto {iCont + 1}: ")
    while True:
        try:
            preco = float(input(f"Digite o preço do produto {iCont + 1}: "))
        except:
            print("Os valores de preço devem ser numericos. Digite novamente.")
        else:
            break
    dicionario_produtos[produto] = preco

valor_total_compra = 0
print("Itens comprados:")
for produto, valor in dicionario_produtos.items():
    print(f"{produto} : R$ {valor:.2f}")
    valor_total_compra  += valor

print(f"O valor total da compra foi R$ {valor_total_compra:.2f}.")
    
