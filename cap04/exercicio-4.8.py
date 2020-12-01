a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
op = input("Qual operação você deseja realizar?")

if op == "adição":
    res = a + b
elif op == "subtração":
    res = a - b
elif op == "multiplicação":
    res = a * b
elif op == "divisão":
    res = a / b
else:
    print("Operação inválida. Tente novamente")
    res = 0
print("O resultado é %2.2f" % res)
