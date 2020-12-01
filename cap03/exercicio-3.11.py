# Faça um programa que solicite o preço de uma mercadoria
# e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preço = float(input("Entre com o preço da mercadoria: "))
desconto = float(input("Entre com o percentual de desconto: "))
valor_desconto = (preço * desconto) / 100
preço_com_desconto = preço - valor_desconto
print("Será descontado R$ %2.2f do preço da mercadoria." % valor_desconto)
print("Você pagará R$ %2.2f pela mercadoria." % preço_com_desconto)
