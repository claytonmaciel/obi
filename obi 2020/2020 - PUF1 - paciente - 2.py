n, c = (int(i) for i in input().split())
infectados = [0]*n

for i in range(c):
    cadeia = tuple(int(i)-1 for i in input().split())
    for j in cadeia[2:]:
        infectados[j] = 1

for n, i in enumerate(infectados):
    if i == 0:
        print(n+1)
