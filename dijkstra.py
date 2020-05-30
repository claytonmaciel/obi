def dijkstra(grafo, no_origem, no_destino):
    nos_nao_visitados = grafo.copy()  # a princípio é o grafo completo já que não visitamos nenhum nó.
    custos = {}  # dicionário para armazenar os custos acumulados de cada nó para alcançar o nó_destino. Será atualizado à medida que avançamos no grafo.
    caminho_percorrido = {}  # dicionário para armazenar o caminho percorrido até o nó_destino
    infinito = 1000  # variável para auxiliar no calculo dos custos
    menor_caminho = []  # dicionário para armazenar o menor caminho entre o nó_origem até o nó_destino

    print(f'Grafo inicial: {nos_nao_visitados}')

    # =============================================================================
    # Inicialmente o nó_origem terá custo Zero e todos os outros nós terão custo infinito.
    # =============================================================================

    for no in nos_nao_visitados:
        custos[no] = infinito

    custos[no_origem] = 0

    print(f'Custos inicial: {custos}')

    # =============================================================================
    # Este laço passará por todos os nós não visitados calculando as distâncias entre os nós no grafo
    # =============================================================================

    while nos_nao_visitados:
        no_atual = None

        # =============================================================================
        # Esse laço serve para encontrar o nó com menor custo do dicionário custos e colocar o nó na variável no_atual
        # =============================================================================

        for no in nos_nao_visitados:
            if no_atual is None:
                no_atual = no

            elif custos[no] < custos[no_atual]:
                no_atual = no

        # =============================================================================
        # Pega os caminhos possíveis a partir do no_atual
        # =============================================================================

        caminhos_possiveis = grafo[no_atual].items()

        # =============================================================================
        # Calcula o custo de cada nó para cada caminho e o custo será atualizado se for menor que o custo existente       
        # =============================================================================

        for no, custo in caminhos_possiveis:
            if custo + custos[no_atual] < custos[no]:
                custos[no] = custo + custos[no_atual]
                caminho_percorrido[no] = no_atual

        print(f'Nó atual: {no_atual}. Custos intermediário: {custos}. Caminho Percorrido {caminho_percorrido}')

        # =============================================================================
        # Retira o nó atual do dicionário de nós não visitados.
        # =============================================================================
        nos_nao_visitados.pop(no_atual)


    print(f'Custos final: {custos}')
    print(f'Caminho percorrido: {caminho_percorrido}')

    # =============================================================================
    # Uma vez que percorreu todos os nós, faremos o menor caminho
    # =============================================================================
    no_atual = no_destino

    while no_atual != no_origem:

        try:
            menor_caminho.insert(0, no_atual)
            no_atual = caminho_percorrido[no_atual]
        except:
            print('Caminho não alcançado!')
            break
    menor_caminho.insert(0, no_origem)

    # =============================================================================
    #  Se o custo for igual ao infinito, é porque o nó não foi alcançado
    # =============================================================================
    if custos[no_destino] != infinito:
        print('O menor custo do menor caminho é ' + str(custos[no_destino]))
        print('O menor caminho é ' + str(menor_caminho))


def main():
    # =============================================================================
    # grafo usando dicionário: 'nó':{'nó_N':custo,'nó_M':custo }
    # =============================================================================
    grafo = {
        '1': {'2': 4, '3': 5},
        '2': {'1': 4, '3': 1, '4': 6},
        '3': {'1': 5, '2': 1, '4': 2, '5': 3},
        '4': {'2': 6, '3': 2},
        '5': {'3': 3}
    }

    dijkstra(grafo, '1', '5')


if __name__ == '__main__':
    main()
