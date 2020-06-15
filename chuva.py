#==========================#
# Questão Chuva            #
#==========================#

lin, col = [int(i) for i in input().split()]
parede = []

def molhar(l,c):
    try:
        if parede[l+1][c] == ".": # restrição 1
            parede[l + 1][c] = 'o'
            molhar(l + 1, c)
    except:
        pass

    try:
        if parede[l][c + 1] == '.' and parede[l + 1][c] == '#':  # restrição 2
            parede[l][c + 1] = 'o';
            molhar(l, c + 1);
    except:
        pass

    try:
        if parede[l][c - 1] == '.' and parede[l + 1][c] == '#': # restrição 3
            parede[l][c - 1] = 'o';
            molhar(l, c - 1);
    except:
        pass

    return


for i in range(lin):
    parede.append(list(input()))

#algoritmo
ini = 0
fim = parede[0].index("o")
molhar(ini,fim)

#imprimir
for x in range(lin):
    for y in range(col):
        print(parede[x][y],end='')
    print()
