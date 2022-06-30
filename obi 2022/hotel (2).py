D = int(input())
A = int(input())
N = int(input())

dias = 32 - N

if N <= 15:
    diaria = D + (A * (N-1))
else:
    diaria = D + (A * 14)

print(diaria*dias)