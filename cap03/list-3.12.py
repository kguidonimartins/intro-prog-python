# -*- coding: utf-8 -*-

# Exemplo de composição de string com
# números inteiros e decimais

nome = "João"

idade = 22

grana = 51.34

print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))

print("%s tem %d anos e R$%2.2f no bolso." % (nome, idade, grana))

print("%s tem %d anos e R$%5.2f no bolso." % (nome, idade, grana))

print("%12s tem %3d anos e R$%2.2f no bolso." % (nome, idade, grana))

print("%24s tem %03d anos e R$%2.2f no bolso." % (nome, idade, grana))

print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))
