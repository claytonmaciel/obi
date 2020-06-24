n = int(input())
grafo = [[] for i in range(n)]
cache = [[-1]*n, [-1]*n]

for i in range(n-1):
    a, b, e = (int(i) for i in input().split())
    grafo[a - 1].append((b - 1, e))
    grafo[b - 1].append((a - 1, e))


def maior_caminho(vertice, empresa_anterior):
    maior = 0    
    for vizinho, empresa in grafo[vertice]:
        if empresa != empresa_anterior:
            caminho = cache[empresa][vizinho]

            if caminho == -1:
                caminho = maior_caminho(vizinho, empresa)
                cache[empresa][vizinho] = caminho        
            if caminho > maior:
                maior = caminho
    
    return maior + 1


resultado = 0
for i in range(n):
    caminho = maior_caminho(i, None)
    if caminho > resultado:
        resultado = caminho

print(resultado)
