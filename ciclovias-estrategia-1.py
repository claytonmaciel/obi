n, m = [int(i) for i in input().split()]

#armazena o caminho de cada nó numa lista
grafo = []
for i in range(n):
    grafo.append([])

for i in range(m):
    a, b = [int(i) for i in input().split()]
    grafo[a-1].append(b-1)
    grafo[b-1].append(a-1)

#ordena os caminhos de cada nó
[no.sort() for no in grafo]

#print(grafo)

#o maior caminho para o próprio nó é tamanho 1
resp = [1 for i in range(n)]
maior = [0 for i in range(n)]

#print(maior)
#print(len(grafo[n-1]))

#percorro os nós em ordem decrescente
for i in range(n-1,-1,-1):
    #armazeno o maior caminho de cada vizinho até o momento
    maior[len(grafo[i])] = 0
    for j in range(len(grafo[i])-1,-1,-1):
        v=grafo[i][j]
        maior[j] = max(resp[v], maior[j+1])

    #percorro o maior caminho de cada vizinho, do vizinho até o nó atual e atualizo na lista resp
    for j in range(len(grafo[i])):
        v=grafo[i][j]
        # e atualizo resp[v] para cada vizinho
        resp[v] = max(resp[v], 2+maior[j+1])

print(' '.join(str(k) for k in resp))
