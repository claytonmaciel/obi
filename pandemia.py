import time

N, M = [int(i) for i in input().split()]
P, R = [int(i) for i in input().split()]
infectados = []
infectados.append(P)

ini = time.time()
for i in range(1,M+1):
    reuniao = [int(j) for j in input().split()[1:]]
    if(i > R-1):
        if any(pessoa in infectados for pessoa in reuniao):
            infectados.extend([pessoa for pessoa in reuniao if pessoa not in infectados])

print(len(infectados))
fim = time.time()
print(fim-ini)