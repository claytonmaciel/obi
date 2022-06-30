N = int(input())
S = int(input())
med = [int(i) for i in input().split()]
soma = 0
saida = 0
o = 0

for i in range(N):
    if o == N-1:
        soma = 0
    soma += med[i]
    if soma == S:
        saida += 1
    elif soma > S:
        soma = 0
        pass
    for o in range(i+1, N):
        soma += med[o]
        if soma == S:
            saida += 1
        elif soma > S:
            soma = 0
            o = 0
            break
print(saida)

