N, F = (int(i) for i in input().split())
vulcao = []

for i in range(N): # entrada: vulcão inicial
    vulcao.append([int(j) for j in input()])

pilha = [(0,0)]

while pilha:
    x,y = pilha.pop()
    if vulcao[x][y] != '*' and F >= int(vulcao[x][y]):
        vulcao[x][y] = '*'
        if x < N - 1:  # se não atingiu o final da linha, verifica abaixo (larva vai para baixo)
            pilha.append((x+1,y))
        if y < N - 1:  # se não atingiu o final da coluna, verifica a direita (larva vai para a direita)
            pilha.append((x,y+1))
        if x > 0:  # se não atingiu inicio da linha, verifica acima (larva vai para cima)
            pilha.append((x-1,y))
        if y > 0:  # se não atingiu inicio da coluna, verifica a esquerda (larva vai para esquerda)
            pilha.append((x,y-1))

for i in range(N):
    print(''.join([str(j) for j in vulcao[i]]))
