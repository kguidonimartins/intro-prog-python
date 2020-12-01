# -*- coding: utf-8 -*-

""" Exemplo de fatiamento """

s = "ABCDEFGHI"

print(s[0:2])

print(s[1:2])  # ?

print(s[1])  # ?

print(s[0])

# O primeiro índice à esquerda dos dois pontos indica o início da fatia e
# o segundo índice, o final.
# O índice que indica o final da fatia não é incluído.

print(s[:4])  # início implícito

print(s[4:])  # final implícito
