n = int(input())
m = int(input())
soma = int(input())

maior = -1

for c in range(n, m + 1):
    digitos = [int(l) for l in str(c)]
    if sum(digitos) == soma:
        maior = c


print(maior)
