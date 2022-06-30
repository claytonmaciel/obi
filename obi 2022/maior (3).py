N = int(input())
M = int(input())
S = int(input())

l = []
for n in range(N, M + 1):
    som = 0
    for let in str(n):
        som += int(let)
    if som == S:
        l.append(n)

print(max(l) if len(l) != 0 else -1)
