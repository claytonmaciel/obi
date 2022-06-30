n = int(input())
s = int(input())
v = [int(i) for i in input().split()]
aux = [0 for i in range(1000000)]
aux[0] = 1

resp = 0
j = 0
for n in v:
    j += n
    if j - s >= 0:
        resp += aux[j - s]
    aux[j] += 1

print(resp)