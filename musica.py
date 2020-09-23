n, m, c = (int(i) for i in input().split())

a = []
d = []

for i in range(n):
    x, y = (int(i) for i in input().split())
    a.append(x)
    d.append(y)

t = 0
percorridos = set((c,))
while True:
    for i in range(n):
        if d[i] == c:
            c = a[i]
            if percorridos.issuperset((c,)):
                print(-1)
                exit()
            percorridos.add(c)
            t += 1
            break
    else:
        break

print(t)
