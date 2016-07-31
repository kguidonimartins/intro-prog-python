# Calcule a seguinte expressão baseando-se nos valores
#definidos na tabela:
# 
# A > B and C or D
# 
# |    A    |    B    |    C    |    D    | Resultados |
# |:-------:|:-------:|:-------:|:-------:|:----------:|
# |    1    |    2    |   True  |  False  |   False    | 
# |    10   |    3    |  False  |  False  |   False    |
# |    5    |    1    |   True  |   True  |   True     |

A = 1
B = 2
C = True
D = False

print(A > B and C or D)

A = 10
B = 3
C = False
D = False

print(A > B and C or D)

A = 5
B = 1
C = True
D = True

print(A > B and C or D)

# \o