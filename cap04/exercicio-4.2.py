velocidade = float(input("Qual era a velocidade do seu veículo?"))

if velocidade > 80:
    print("Você será multado.")
    excesso = velocidade - 80
    multa = excesso * 5
    print("O valor da multa é de R$ %2.2f." %multa)
