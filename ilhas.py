#==========================#
# Questão Ilhas            #
#==========================#

def dijkstra(grafo, servidor):
    nos_nao_visitados = grafo.copy()  # a princípio é o grafo completo já que não visitamos nenhum nó.
    custos = {}  # Armazena os custos acumulados de cada nó a partir do servidor. Será atualizado à medida que avançamos no grafo.
    infinito = 50000  # variável para inicializar todos os custos

    for no in nos_nao_visitados:
        custos[no] = infinito

    custos[servidor] = 0

    while nos_nao_visitados:
        no_atual = None

        for no in nos_nao_visitados:
            if no_atual is None:
                no_atual = no
            elif custos[no] < custos[no_atual]:
                no_atual = no

        caminhos_possiveis = grafo[no_atual].items()

        for no, custo in caminhos_possiveis:
            # quando o custo acumulado for menor que o existente, eu atualizo o valor do custo.
            if custo + custos[no_atual] < custos[no]:
                custos[no] = custo + custos[no_atual]

        nos_nao_visitados.pop(no_atual)

    #print(f'Custos final: {custos}')

    # pegando o custo máximo e o custo mínimo no dicionário Custos. Ignorando o custo 0 do próprio nó servidor
    max_custo = max(custos[no] for no in custos)
    min_custo = min(custos[no] for no in custos if custos[no] != 0)

    return max_custo - min_custo

def main():
    n, m = [int(i) for i in input().split()]
    grafo = {}

    # =============================================================================
    # grafo: 'nó':{'nó_N':custo,'nó_M':custo }
    # exemplo 1 da questão:
    # grafo = {
    #    '1': {'2': 5, '3': 4},
    #    '2': {'1': 5, '3': 6, '4': 8},
    #    '3': {'1': 4, '2': 6, '4': 12},
    #    '4': {'2': 8, '3': 12}
    # }
    # =============================================================================
    for i in range(m):
        a, b, c = [i for i in input().split()]
        aux = {b:int(c)}
        if a not in grafo:
            grafo[a] = aux
        else:
            aux2 = grafo[a]
            aux2[b] = int(c)
        aux = {a: int(c)}
        if b not in grafo:
            grafo[b] = aux
        else:
            aux2 = grafo[b]
            aux2[a] = int(c)

    servidor = input()
    #Seu programa deve produzir uma única linha, contento um inteiro,
    # a diferença entre o ping da ilha com maior ping até o servidor,
    # e o da ilha com menor ping até o servidor.
    #print(grafo)

    print(dijkstra(grafo, servidor))

if __name__ == '__main__':
    main()
