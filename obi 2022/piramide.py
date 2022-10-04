dimensao = int(input())

torre = []

for x in range(dimensao):
    linha = []
    for y in range(dimensao):
        linha.append(1)

    torre.append(linha)
fim = True

c = 0

while fim:
    fim = False
    for l in range(dimensao):
        if l <= c or l >= (dimensao - (c + 1)):
            continue
        else:
            for n in range(dimensao):
                if n <= c or n >= (dimensao - (c + 1)):
                    continue
                else:
                    torre[l][n] += 1
                    fim = True

    c += 1

for l in torre:
    for x in range(dimensao):
            if x == dimensao - 1:
                print(l[x])
            else:
                print(l[x], end=' ')