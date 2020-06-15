import time

n, m = (int(i) for i in input().split())
ciclovias = [[] for i in range(n)]

for i in range(m):
    a, b = (int(i) - 1 for i in input().split())
    ciclovias[a].append(b)
    ciclovias[b].append(a)


def copiar_grafo(grafo):
    return [i.copy() for i in grafo]


def encontrar_caminho(grafo, atual, anterior=-1):
    maior_caminho = 1
    for i in grafo[atual].copy():
        grafo[atual].remove(i)
        grafo[i].remove(atual)
        if i > anterior:
            caminho = encontrar_caminho(copiar_grafo(grafo), i, atual) + 1
            if caminho > maior_caminho:
                maior_caminho = caminho
        
    return maior_caminho


for i in range(n):
    print(encontrar_caminho(copiar_grafo(ciclovias), i), end=' ')
