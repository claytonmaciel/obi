N, M, I = [int(i) for i in input().split()]
idades = [int(i) for i in input().split()]

gerente = []
gerenciado = []
acoes = []

for i in range(M):
    a, b = [int(k) for k in input().split()]
    gerente.append(a)
    gerenciado.append(b)

for i in range(I):
    acoes.append([k for k in input().split()])

def busca_gerente_mais_novo(func):
    global menor_global
    #pega os chefes direto recursivamente
    for x in range(M):
        if gerenciado[x] == func:
            if menor_global > idades[gerente[x]-1]:
                menor_global = idades[gerente[x]-1]
            busca_gerente_mais_novo(gerente[x])

def troca_gerencia(f1, f2):
    for i in range(M):
        if gerente[i] == f1:
            gerente[i] = f2
        elif gerente[i] == f2:
            gerente[i] = f1
        if gerenciado[i] == f1:
            gerenciado[i] = f2
        elif gerenciado[i] == f2:
            gerenciado[i] = f1

for a in acoes:
    if a[0] == 'P':
        if int(a[1]) not in gerenciado:
            print('*')
        else:
            menor_global = 5000
            busca_gerente_mais_novo(int(a[1]))
            print(menor_global)
    else:
        troca_gerencia(int(a[1]),int(a[2]))