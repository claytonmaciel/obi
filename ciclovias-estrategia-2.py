#==========================#
# Questão Ciclovias        #
#==========================#

n, m = [int(i) for i in input().split()]
grafo = []
resp = []

for i in range(n):
    grafo.append([])

#armazena o caminho de cada nó numa lista
for i in range(m):
    a, b = [int(i) for i in input().split()]
    grafo[a-1].append(b-1)
    grafo[b-1].append(a-1)

#metodo de busca do maior caminho
def busca(no1, no2):
    global cam, caminho
    # pego todos os vizinhos do nó2 maiores que o nó1
    vizinhos_maiores_que_no1 = [no for no in grafo[no2] if no > no1]
    for no in vizinhos_maiores_que_no1:
        cam += 1
        busca(no2, no)
        caminho = max(caminho,cam)
        cam -= 1

for i in range(n):
    caminho = 1
    for no in grafo[i]:
        if max(grafo[no]) >= i: # se o maior dos nós vizinhos for maior que o nó i então o algoritmo vai efetuar a busca, senão n tem o que procurar
            cam = 2
            busca(i, no)
            caminho = max(caminho, cam)
        else:
            caminho = 2
    resp.append(caminho)

print(' '.join(str(k) for k in resp))
