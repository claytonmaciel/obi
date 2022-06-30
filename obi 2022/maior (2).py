N = int(input())
M = int(input())
S = int(input())
soma = 0
resposta = -1
for i in range(N, M+1):
    num = str(i)
    num.split()
    for o in num:
        soma += int(o)
    if soma == S:
        if i > resposta:
            resposta = i
            soma = 0
    else:
        soma = 0
print(resposta)