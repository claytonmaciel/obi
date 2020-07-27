n = int(input())
grafo = [[] for i in range(n)]

for i in range(n-1):
    a, b, c = (int(i) for i in input().split())
    grafo[a-1].append((b-1, c))
    grafo[b-1].append((a-1, c))

# Classe pra guardar os dados do vertice
class DadosV:
    # No contrutor, tudo é atribuido como se a recursao comecasse
    def __init__(self, vertice, vertice_anterior, empresa):
        self.vertice=vertice
        self.vertice_anterior=vertice_anterior
        self.empresa = empresa
        self.maior_caminho = [0, 0]
        self.it = iter(grafo[vertice]) # em que posicao da lista de vertices esta. #o ponteiro do vizinho do vertice

resp = 0
pilha = [ DadosV(0, -1, None) ] # inclui a primeira chamada na pilha

while pilha: # enquanto a pilha não esta vazia a dfs nao acabou
    topo = pilha[-1] # pega os dados do topo da pilha
    try:
        vizinho, empresa = next(topo.it) # pega o próximo vizinho do vertice
        if vizinho != topo.vertice_anterior:
           pilha.append( DadosV (vizinho, topo.vertice, empresa) ) # adiciona na pilha, imitando a chamada recursiva
    except StopIteration:  # quando acabam todos os vizinhos gera uma excecao StopIteration, fazendo uma espécie de backtracking
        topo_removido = pilha.pop()  # remove o topo (retorna da recursao)
        sub_caminho, empresa = topo_removido.maior_caminho, topo_removido.empresa # pego subcaminho e empresa do vertice removido da pilha
        resp = max(resp, topo_removido.maior_caminho[0] + topo_removido.maior_caminho[1] + 1) # atualiza resp antes de retornar
        if pilha: # redefino o novo topo da pilha atualizando as informacoes de maior caminho no topo da pilha
            topo = pilha[-1]
            topo.maior_caminho[empresa] = max(topo.maior_caminho[empresa], sub_caminho[1-empresa] + 1)

print(resp)