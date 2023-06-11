# Elnatan

m,n = [int(x) for x in input().split()]
e = [[int(x) for x in input().split()] for _ in range(m)]
p = int(input())
ps = [[int(x)-1 for x in input().split()] for _ in range(p)]
v = 0
for i in ps:
    if e[i[0]][i[1]] > 0:
        v += 1
        e[i[0]][i[1]] -= 1
print(v)