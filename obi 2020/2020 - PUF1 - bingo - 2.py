n, k, u = (int(i) for i in input().split())
tabelas = [[int(i) for i in input().split()] for j in range(n)]
sorteados = (int(i) for i in input().split())

ganhadores = []
for i in sorteados:
    if len(ganhadores) == 0:
        for n, tabela in enumerate(tabelas.copy()):
            if i in tabela:
                tabela.remove(i)
                if len(tabela) == 0:
                    ganhadores.append(str(n+1))
    else:
        break

print(' '.join(ganhadores))
