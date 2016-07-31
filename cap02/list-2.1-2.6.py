#!/usr/bin/python
# -*- coding: utf-8 -*-

# Para as duas linhas anteriores, ver:
# https://www.vivaolinux.com.br/topico/Python/Python-SyntaxError-NonASCII-character-alguem-pode-me-ajudar

# Comandos básicos do segundo capítulo

# Listagem 2.1 - Adição
print(2 + 3)

# Listagem 2.2 - Subtração
print(5-3)

# Listagem 2.3 - Adição e subtração
print(10-4+2)

# Listagem 2..4 - Multiplicação e divisão
print(2*10)
print(20/4)

# Listagem 2.5 - Exponenciação
print(2**3)

# Listagem 2.6 - Resto da divisão inteira
print(10 % 3)
print(16 % 7)
print(63 % 8)

# Exercício 2.1
## Converta: 10 + 20 *30
print(10 + 20 * 30) 
print(10 + (20 *30))
print((10 + 20) * 30)

## Converta: 4 ** 2 / 30
print(4 ** 2 / 30)

## Converta (9 ** 4 + 2) + 6 - 1
print((9 ** 4 + 2) + 6 - 1)

# Exercício 2.2
## Copie e cole interpretador a seguinte expressão: 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
## Ordem de precedência das operações: ** > * > / e % > + > -
print(10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)
print(((10 % 3) * (10 ** 2)) + 1 - ((10 * 4) / 2))
print((((((((10 % 3) * 10) ** 2) + 1) - 10) * 4) / 2))



