# Quanto pagar pelo aluguel do carro?
# diária = R$ 60 por dia
# km rodado = R$ 0.15

km = float(input("Quilômetros percorridos:"))

dias = int(input("Dias com o carro:"))

valor = (km * 0.15) + (dias * 60)

print("Valor pelo carro alugado é R$ %2.f" % valor)
