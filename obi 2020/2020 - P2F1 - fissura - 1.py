N, F = (int(i) for i in input().split())
vulcao = []

for i in range(N):
    vulcao.append([int(i) for i in input()])

def avancar(x, y):
    aux = vulcao[x][y]
    if aux != '*' and F >= int(aux):
        vulcao[x][y] = '*'
        if x < N - 1:
            avancar(x + 1, y)
        if y < N - 1:
            avancar(x, y + 1)
        if x > 0:
            avancar(x - 1, y)
        if y > 0:
            avancar(x, y - 1)


avancar(0, 0)

for i in range(N):
    for j in range(8):
        print(vulcao[i][j], end='')
    print()
