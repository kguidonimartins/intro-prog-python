valor_casa = float(input("Qual é o valor da casa?"))
salario = float(input("Qual é a sua renda mensal?"))
anos = float(input("Em quantos anos você pretende pagar a casa?"))

parcela = valor_casa / (anos * 12)
porc_30_sal = (salario * 30) / 100

if parcela > porc_30_sal:
    print("O empréstimo não pode ser aprovado")
elif parcela < porc_30_sal:
    print("O empréstimo pode ser aprovado")
