N = int(input())
v = [] #lista onde será armazenado os números
va = [] #lista onde será armazenado os valores já verificados
res = 0 #resposta final

#adicionando valores na lista v
for x in range(N):
    v.append(int(input()))

#Se a lista tiver com menos de 300 valores, i precisará ir de 0 até a raiz quadrada de N mais 10
#Se a lista tiver com mais de 300 valores, i precisará ir de 0 até a raiz quadrada de N
if N < 300:
    Na = round(N**0.5)+10
else:
    Na = round(N**0.5)

#Estratégia: para cada par de números da lista (i,j), eu verifico em toda a lista (k) a quantidade de vezes que foi encontrado o par (cont.)
#a quantidade de vezes só é somada se o elemento vk for igual ao elemento vi ou ao elemento vj e se ele não foi o mesmo número adicionado por último.
#O iterativo i só precisa percorrer até a raiz quadrada da quantidade de elementos da lista (cont.)
# para encontrar quantidade máxima possível de números numa sequência marcada.

for i in range(Na):
    for j in range(i,N):
        if v[i] != v[j]:
            if str(v[i]) + "" + str(v[j]) in va or str(v[j]) + "" + str(v[i]) in va:
                continue
            va.append(str(v[i]) + "" + str(v[j]))
            uadd = -1  # Ultimo elemento que foi adicionado
            respl = 0  # Quantidade de ocorrências para os valores vi  e vj
            for k in range(N):
                if (v[k] == v[i] or v[k] == v[j]) and v[k] != uadd:# Se vk for igual de vi ou vj and não igual ao último adicionado.
                    respl += 1  # Adiciono o valor para os elementos vi e vj
                    uadd = v[k] # Armazena o último elemento adicionado
        else:
            respl = 1
        res = max(res, respl)
print(res)
