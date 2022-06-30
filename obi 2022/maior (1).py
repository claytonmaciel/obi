N = int(input())
M = int(input()) + 1
S = int(input())

try:
    print(max((i for i in range(N, M) if sum(map(int, list(str(i)))) == S)))

except ValueError:
    print(-1)
