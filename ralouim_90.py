N = int(input())
melhor = [0] * (N + 1)
pmelhor = [0] * (N + 1)

pontos = [[0, 0]]
for i in range(N):
    x, y = [int(i) for i in input().split()]
    pontos.append([x, y])

dists = [[0] * (N + 1) for _ in range(N + 1)]
pares = []
for a in range(N + 1):
    for b in range(a + 1, N + 1):
        dx = pontos[a][0] - pontos[b][0]
        dy = pontos[a][1] - pontos[b][1]
        if a != b:
            dists[a][b] = dx * dx + dy * dy
        pares.append((dists[a][b], a, b))

pares = sorted(pares, key=lambda x: x[0])

for par in pares:
    d, a, b = par

    if d != dists[a][0]:
        dists[a][0] = d
        pmelhor[a] = melhor[a]
    if d != dists[b][0]:
        dists[b][0] = d
        pmelhor[b] = melhor[b]

    if a == 0:
        melhor[a] = max(melhor[a], pmelhor[b])
    else:
        melhor[a] = max(melhor[a], 1 + pmelhor[b])
        melhor[b] = max(melhor[b], 1 + pmelhor[a])

print(1 + melhor[0])
