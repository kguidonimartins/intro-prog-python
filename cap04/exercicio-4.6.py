distancia = float(input("Qual é a distância da sua viagem?"))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print("O valor da sua passagem será %2.2f" % valor)
