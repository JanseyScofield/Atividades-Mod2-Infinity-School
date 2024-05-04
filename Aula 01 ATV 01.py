idade = int(input("Digte sua idade: "))

if idade < 12:
    resp = "criança"
elif idade >= 12 and idade <=17:
    resp = "adolescente"
elif idade >=18 and idade <=59:
    resp = "adulto"
else:
   resp = "idoso"


print(f"Você é {resp}.")
