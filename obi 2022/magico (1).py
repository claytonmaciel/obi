N = int(input())
num = ""
linha = ""
coluna = ""
soma1= 0
soma2= 0
for i in range(N):
    l = [int(i) for i in input().split()]
    if 0 in l:
        linha = i+1
        soma1 = sum(l)
        for c in range(N):
            if l[c] == 0:
                coluna = c+1
    if 0 not in l:
        soma2 = sum(l)

print(soma2 - soma1)
print(linha)
print(coluna)
