INF = 50000

n, m = (int(i) for i in input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    u, v, p = (int(i) for i in input().split())
    g[u - 1].append((v - 1, p))
    g[v - 1].append((u - 1, p))

s = int(input()) - 1

nao_percorridos = list(range(n))
pings = [INF] * n
pings[s] = 1

while nao_percorridos:
    atual = min(nao_percorridos, key=lambda i: pings[i])
    for adj, p in g[atual]:
        if pings[adj] > pings[atual] + p :
            pings[adj] = pings[atual] + p
    nao_percorridos.remove(atual)

pings.pop(s)
print(max(pings) - min(pings))
