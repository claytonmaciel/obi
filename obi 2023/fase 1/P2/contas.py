#José Roberto

V, *contas = (int(input()) for _ in range(4))
contas.sort()

if sum(contas) <= V:
    resp = 3

elif sum(contas[:2]) <= V:
    resp = 2

elif contas[0] <= V:
    resp = 1

else:
    resp = 0

print(resp)

