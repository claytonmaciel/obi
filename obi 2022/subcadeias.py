tamanho = int(input())
cadeia = [x for x in input()]

tam_palin = 0
tam_max = 0

def reverter(lista):
    n = 0
    lista_nova = [i for i in lista]
    for l in range(len(lista)):
        lista_nova.insert(n, lista_nova[-1])
        lista_nova.pop(-1)
        n += 1
    # print(lista)
    return lista_nova

# for x in range(len(cadeia)):
#     n = x + 1
#     while n != tamanho:
#         n += 1
#         print(cadeia[x:n], cadeia[x:n].reverse())
#         teste_atual = cadeia[x:n]
#         teste_atual_reverse = teste_atual.reverse()
#         if teste_atual_reverse != teste_atual:
#             if tam_palin > tam_max:
#                 tam_max = tam_palin
#             break
#         else:
#             tam_palin += 1
#
# print(tam_max)

for x in range(len(cadeia)):
    n = tamanho
    while n != x:
        teste_atual = cadeia[x:n]
        teste_atual_reverse = reverter(teste_atual)
        if teste_atual_reverse != teste_atual:
            n -= 1
            continue
        else:
            tam_palin = (n - x)
        n -= 1
        if tam_palin >= tam_max:
            tam_max = tam_palin

print(tam_max)