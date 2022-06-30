N = int(input())

matrix = []
for i in range(N):
    insertion = [int(i) for i in input().split()]
    matrix.append(insertion)

magic_number = 0
for line in matrix:
    if 0 in line:
        continue
    else:
        magic_number = sum(line)

ilegible = 0
pos = 0
for line in matrix:
    if 0 in line:
        ilegible = sum(line) - magic_number
        pos = [pos, line.index(0)]
        break
    else:
        pos += 1

print(-ilegible)
print(pos[0] + 1)
print(pos[1] + 1)