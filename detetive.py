# =============ENTRADA==================================================

E, I, V = (int(i) for i in input().split())

conexoes = tuple(([], []) for i in range(E))

for i in range(I):
    a, b = (int(i)-1 for i in input().split())
    conexoes[a][1].append(b)
    conexoes[b][0].append(a)

ocorridos = [int(i)-1 for i in input().split()]

# =============LOGICA==================================================

i = 0
while i < len(ocorridos):
    '''
    Percorre a arvore no sentido inverso (consequencia->causas)
    '''
    evento = ocorridos[i]
    causas = conexoes[evento][0]
    
    '''
    Testa se existem multiplas causas, caso não então esta deve ser
    adicionada a lista de ocorridos
    '''
    while len(causas) == 1:
        evento = ocorridos[i] = causas[0]
        causas = conexoes[evento][0]
    
    '''
    Caso existam multiplas causas, o programa deve percorrer todas as
    causas de causas até encontrar uma causa em comum
    '''
    if len(causas) > 0:
        terminais = set()
        while causas:
            causa = causas.pop(0)
            super_causas = conexoes[causa][0]
            if super_causas:
                causas.extend(super_causas)
            else:
                terminais.add(causa)
        
        if len(terminais) == 1:
            terminal = terminais.pop()
            if terminal not in ocorridos:
                ocorridos.append(terminal)
    
    i += 1

'''
Percorre a arvore no sentido causa->consequencia, adicionando todos os
eventos encontrados na lista de ocorridos
'''
for evento in ocorridos:
    consequencias = conexoes[evento][1]
    ocorridos.extend(consequencias)

# =============SAIDA===================================================

for i in sorted(set(ocorridos)):
    print(i+1, end=' ')
print()
