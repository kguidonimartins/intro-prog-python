a = float(input("Entre com o primeiro número:"))
b = float(input("Entre com o segundo número:"))
c = float(input("Entre com o terceiro número:"))

maior = 0

if a > b:
    if a > c:
        maior = a

if b > c:
    if b > a:
        maior = b

if c > a:
    if c > b:
        maior = c

print("Maior número é %f" % maior)

menor = 0

if a < b:
    if a < c:
        menor = a

if b < a:
    if b < c:
        menor = b

if c < a:
    if c < b:
        menor = c

print("Menor número é %f" % menor)

# a=int(input("Digite o primeiro valor:"))
# b=int(input("Digite o segundo valor:"))
# c=int(input("Digite o terceiro valor:"))
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# menor = a
# if b < c and b < a:
#     menor = b
# if c < b and c < a:
#     menor = c
# print("O menor número digitado foi %d" % menor)
# print("O maior número digitado foi %d" % maior)
