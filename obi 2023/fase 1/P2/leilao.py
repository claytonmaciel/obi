#José Roberto

N = int(input())

C, V = '', -1
for _ in range(N):
    c, v = (input() for _ in range(2))
    v = int(v)

    if v > V:
        C = c
        V = v

print(C)
print(V)