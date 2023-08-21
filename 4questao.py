
num1 = float(input("Digite um número:"))

op = input("Digite uma operação matemárica: (+,-)")

num2 = float(input("Digite um número:"))

if op == "+":
    print("O resultado da soma é: ", (num1+num2))
elif op == "-":
    print("O resultado da subtração é: ", (num1-num2))
else:
    print("Você não digitou uma operação valida ")
    
        