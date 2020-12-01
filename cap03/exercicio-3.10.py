# Faça um programa que calcule o aumento de um salário. Ele deve
# solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salário = int(input("Entre com o salário atual (sem ponto e sem vírgula): ")) 
porcen_aumento = float(input("Entre com o porcentagem do aumento: "))
aumento = (salário * porcen_aumento) / 100
novo_salário = salário + aumento
print("%2.2f porcento de aumento equivale a R$ %2.2f" % (porcen_aumento, aumento))
print("O novo salário será R$ %2.2f" % novo_salário)
