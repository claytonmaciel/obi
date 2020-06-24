n, k, u = (int(i) for i in input().split())
cartelas = []
ganhador = []

for i in range(n): #lendo os números das cartelas
    cartelas.append([int(j) for j in input().split()])

numssort = [int(i) for i in input().split()] #lendo os números sorteados

for num in numssort: # para cada número sorteado retira-se o número de cada cartela
    for i in range(n):
        try:
            cartelas[i].remove(num) # remove o número sorteado da cartela
        except:
            continue
        if not cartelas[i]: #se a cartela ficar vazia é pq temos um ganhador
            ganhador.append(i+1)
    if ganhador: #verifica ganhador, se houver ganhador, para o laço
        break

print(' '.join(str(k) for k in sorted(ganhador)))