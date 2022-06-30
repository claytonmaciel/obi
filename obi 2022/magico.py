d = int(input())
q = []

coord_zero = []
for c in range(d):
    linha = [int(i) for i in input().split()]
    if 0 in linha:
        coord_zero = [linha.index(0), c]
    q.append(linha)

soma = 0
soma_linha_zero = 0
faltando = 0

for c in range(1, d):
    if c != coord_zero[1]:
        for n in q[c]:
            soma += n
        break

for n in q[coord_zero[1]]:
    if n != 0:
        soma_linha_zero += n

faltando = soma - soma_linha_zero

print(faltando)
print(coord_zero[1] + 1)
print(coord_zero[0] + 1)



