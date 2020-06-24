n = int(input())
grafo = [[] for i in range(n)]

#armazena os nós adjacentes na lista grafo
for i in range(n-1):
    a, b, c = [int(j) for j in input().split()]
    grafo[a-1].append([b-1, c])
    grafo[b-1].append([a-1, c])


def busca(no1, no2):
    global caminho, maior_caminho
    # lista de todos os vizinhos que a viagem seja de uma empresa diferente
    vizinhos_viagem_diferente = [no for no in grafo[no2[0]] if no[0] != no1 and no[1] != no2[1]]
    for no in vizinhos_viagem_diferente:
        caminho += 1
        busca(no2[0], no)
        maior_caminho = max(maior_caminho, caminho)
        caminho -= 1


maior_caminho = 1
for i in range(n):
    for vizinho in grafo[i]:
        caminho = 2
        busca(i,vizinho)
        maior_caminho = max(maior_caminho, caminho)

print(maior_caminho)
