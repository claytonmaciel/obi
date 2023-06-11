#José Roberto

m, n = (int(i) for i in input().split())

estoque = [[int(i) for i in input().split()] for _ in range(m)]

pedidos = 0
for _ in range(int(input())):
    i, j = (int(i)-1 for i in input().split())

    if estoque[i][j]:
        pedidos += 1
        estoque[i][j] -= 1

print(pedidos)
