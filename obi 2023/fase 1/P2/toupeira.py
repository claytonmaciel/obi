#José Roberto

S, T = (int(i) for i in input().split())

matriz = [[False] * S for i in range(S)]

for i in range(T):
    x, y = (int(j)-1 for j in input().split())
    matriz[x][y] = True
    matriz[y][x] = True


cont = 0
for _ in range(int(input())):
    c, *sugestao = (int(i)-1 for i in input().split())

    for i in range(c):
        x, y = sugestao[i:i+2]
        if not matriz[x][y] or not matriz[y][x]:
            break

    else:
        cont += 1

print(cont)