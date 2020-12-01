#!/usr/bin/python
# -*- coding: utf-8 -*-

# Exemplos de entrada de dados com números inteiros ou decimais

anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print("Bônus de R$ %5.2f" % bonus)
