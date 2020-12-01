# tempo de vida de um fumante

n_cigarros = int(input("Quantos cigarros você fuma por dia?"))

tempo_adicto = int(input("Há quanto tempo você é fumante?"))

n_cigarros_anos = 10 * tempo_adicto * 365 * n_cigarros

minutos_dia = 24 * 60

tempo_perdido = (10 * n_cigarros_anos) / minutos_dia

print("Você já perdeu %d dias da sua vida por causa do cigarro!" %tempo_perdido)
