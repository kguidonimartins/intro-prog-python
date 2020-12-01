tipo = input("Qual é o tipo de instalação?")
kwh = float(input("Informe seu consumo em kWh:"))

if tipo == "residencial" and kwh <= 500:
    preco = 0.4
elif tipo == "residencial" and kwh > 500:
    preco = 0.65
elif tipo == "comercial" and kwh <= 1000:
    preco = 0.55
elif tipo == "comercial" and kwh > 1000:
    preco = 0.6
elif tipo == "industrial" and kwh <= 5000:
    preco = 0.55
elif tipo == "industrial" and kwh > 5000:
    preco = 0.60

print("Você deve pagar %2.2f pelo fornecimento de energia" % preco)
