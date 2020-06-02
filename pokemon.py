doces = int(input())
pokes = []

for i in range(3):
    pokes.append(int(input()))

#Estratégia: distribuir os doces primeiro para os pokemons que precisam menos de doce para evoluir
pokes.sort()
resp = 0

for i in range(3):
    if pokes[i] <= doces:
        resp += 1
        doces -= pokes[i]

print(resp)