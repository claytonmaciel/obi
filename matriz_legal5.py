l, c = [int(i) for i in input().split()]
m = []  #matriz principal
mb = [] #matriz binária
h = []  #matriz altura da matriz binária
j0 = [] #matriz de índices para todos [i,j0] < [i,j] na matriz h
j1 = [] #matriz de índices para todos [i,j1] < [i,j] na matriz h
resp = 0

for i in range(l):
    m.append([int(j) for j in input().split()])
    if i < l - 1:
        mb.append([0 for j in range(c - 1)])
        h.append([0 for j in range(c - 1)])
        j0.append([0 for j in range(c - 1)])
        j1.append([0 for j in range(c - 1)])

# preenchendo a matriz binária
for i in range(l - 1):
    for j in range(c - 1):
        if m[i][j] + m[i + 1][j + 1] <= m[i][j + 1] + m[i + 1][j]:
            mb[i][j] = 1


# calculando a matriz h
for i in range(l - 1):
    for j in range(c - 1):
        if not mb[i][j]:
            continue
        # calculo do h[i][j] baseado nas linhas acima da mesma coluna [i-1][j]
        if mb[i - 1][j] == 1:
            h[i][j] = 1 + h[i - 1][j]
        else:
            h[i][j] = 1

# calculando o índice j0 mais à direita tal que 1≤j0<j e h(i,j0)<h(i,j)

for i in range(l - 1):
    pilha = []
    for j in range(c - 1):
        while pilha and pilha[-1][1] >= h[i][j]:  # enquanto o elemento do topo na pilha tiver um valor de h anterior maior que o h atual, retire a pilha
            pilha.pop()
        # se j0 não existe, digamos que ele será uma posição a menos do limite(1)
        if pilha:
            j0[i][j] = pilha[-1][0]

        pilha.append((j + 1, h[i][j]))

# calculo do índice j1 mais à esquerda tal que j<j1≤M e h(i,j1)<h(i,j)

for i in range(l - 1):
    pilha = []
    for j in range(c - 2, -1, -1):
        while pilha and pilha[-1][1] >= h[i][j]:  # enquanto o elemento do topo na pilha tiver um valor de h anterior maior que o h atual, retire a pilha
            pilha.pop()

        # se a pilha não existe, então pega o valor da coluna
        if not pilha:
            j1[i][j] = c-1
        else:
            j1[i][j] = pilha[-1][0]

        pilha.append((j, h[i][j]))

# resposta da questão
for i in range(l-1):
    for j in range(c-1):
        if h[i][j]:
            resp = max(resp, ((j1[i][j] - j0[i][j])+1) * (h[i][j] + 1))  # (x_m+1)*(y_m+1)

print(resp)