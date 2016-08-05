# Escreva um programa que leia um valor em metros e
#o exiba em milímetros.

metros = float(input("Entre com o valor em metros: "))
milímetros = metros * 1000
print("%2.2f em metro(s) é igual a %2.1f em milímetros" % (metros, milímetros))