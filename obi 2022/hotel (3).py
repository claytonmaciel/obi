D = int(input())
A = int(input())
N = int(input())

# Equação: f(n) = 32 - N * (D + N*A) reais
NN = N if N <= 15 else 15
print((31 + 1 - N) * (D + (NN - 1) * A))
