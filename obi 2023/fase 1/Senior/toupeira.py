#Elnatan

_, t = [int(x) for x in input().split()]
# l = []
# for _ in range(t):
#     x,y = [int(x) for x in input().split()]
#     l.append((x,y))
#     l.append((y,x))
l = {frozenset(int(x) for x in input().split()):False for _ in range(t)}
p = int(input())
retorno = p
for _ in range(p):
    sugestao = [int(x) for x in input().split()]
    q = sugestao.pop(0)
    for i in range(1,q):
        if l.get(frozenset((sugestao[i],sugestao[i-1])),True):
            retorno -=1
            break
print(retorno)