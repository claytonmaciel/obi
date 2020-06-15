#==================================#
# Questão Distância entre amigos   #
#==================================#

N = int(input())
predios = [int(i) for i in input().split()]

m_dist = 0
for x in range(N-1):
    for y in range(x+1,N):
        dist = predios[x]+predios[y]+(y-x)
        if dist > m_dist:
            m_dist = dist

print(m_dist)
