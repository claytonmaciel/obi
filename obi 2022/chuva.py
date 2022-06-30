n_medicoes = int(input())
soma = int(input())
valores = [int(i) for i in input().split()]

intervalos = []
total = 0

for c in range(n_medicoes):
    for r in range(c, n_medicoes):
        intervalos.append([c, r])

for i in intervalos:
    soma_parcial = 0
    if i[1] == i[0]:
        soma_parcial = valores[i[0]]
    else:
        soma_parcial = sum(valores[i[0]:i[1] + 1])
    if soma_parcial == soma:
        total += 1

print(total)

# intervalos = 0
#
# for c in range(len(valores)):
#     s_parcial = valores[c]
#
#     if s_parcial == soma:
#         intervalos += 1
#
#     for n in range(c + 1, len(valores)):
#         if s_parcial + valores[n] == soma:
#             s_parcial += valores[n]
#             intervalos += 1
#         elif s_parcial + valores[n] < soma:
#             s_parcial += valores[n]
#             continue
#         else:
#             break
#
#
# print(intervalos)