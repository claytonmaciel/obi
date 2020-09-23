n = int(input())
g = [[0] * n for _ in range(n)]
tendas = []

for _ in range(n):
    a, b = (int(i) for i in input().split())
    tendas.append((a, b))

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = tendas[i]
        x2, y2 = tendas[j]
        g[i][j] = g[j][i] = (x1 - x2)**2 + (y1 - y2)**2

g.insert(0, [x**2 + y**2 for x, y, in tendas])

dist = 1e9
atual = 0
doces = 1

while True:
    dist_proximo = max(g[atual])
    proximo = g[atual].index(dist_proximo)

    if dist_proximo == 0:
        break
    
    if dist_proximo < dist:
        dist = dist_proximo
        atual = proximo
        doces += 1
    else:
        g[atual][proximo] = 0

print(doces)