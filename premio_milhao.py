#==========================#
# Questão Prêmio do Milhão #
#==========================#

dias = int(input())
acessos = []
for i in range(dias):
    acessos.append(int(input()))

quant_dias = 0
soma = 0
for a in acessos:
    if soma >= 1000000:
        break
    soma += a
    quant_dias += 1

print(quant_dias)
