# Operadores lógicos combinados em expressões lógicas complexas.
# Operadores relacionais (==, !=, >=, etc) precedem os lógicos.
# Precedência de avaliação: 
# not --> and --> or
# True or False and (not True)
# True or (False and False)
# (True or False)
# (True)
# Operadores relacionais precedem os lógicos:

salário = 100
idade = 20
print(salário > 1000 and idade > 18)

# Desmembrando:
# (100 > 1000) and (20 > 18)
# (True and False)
# False

salário = 2000
idade = 30
print(salário > 1000 and idade > 18)


