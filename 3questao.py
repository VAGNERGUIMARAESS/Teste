idade=int(input("Digite sua idade: "))

if idade < 10:
    print("Você é criança")
elif idade >= 10 and idade <17:
    print("Você é adolescente")
elif idade >= 17 and idade <50:
    print("Você é adulto")
elif idade >= 50 and idade <= 100:
    print("Você é idoso")
else:
    print("Valor não encontrado!") 

