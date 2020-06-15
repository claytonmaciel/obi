#==========================#
# Questão Soma             #
#==========================#

n, k = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
quant = 0
soma = 0

for x in range(n):
    soma = v[x]
    if soma > k:
        continue
    for y in range(x+1,n+1):
        if soma > k:
            break
        if soma == k:
            quant += 1
        if y < n:
            soma += v[y]

print(quant)
