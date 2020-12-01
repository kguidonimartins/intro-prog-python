salario = float(input("Digite seu salário:"))

if salario > 1250:
    aumento = (10 * salario) / 100
    novo_salario = salario + aumento

if salario <= 1250:
    aumento = (15 * salario) / 100
    novo_salario = salario + aumento

print("Seu aumento é de %2.2f" % aumento)
print("Seu novo salário é de %2.2f" % novo_salario)
