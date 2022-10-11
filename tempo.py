amigos = [[0, False, False] for _ in range(100)] # [[tempo, enviou, respondido]]
n = int(input())

for _ in range(n):
  tipo, x = input().split()
  x = int(x) - 1
  
  if tipo != 'T':
    for i in range(100):
      if amigos[i][1]:
        amigos[i][0] += 1

    if tipo == 'R':
      amigos[x][1] = True
      amigos[x][2] = False
    else:
      amigos[x][1] = False
      amigos[x][2] = True

  else:
    for i in range(100):
      if amigos[i][1]:
        amigos[i][0] += x

for i in range(100):
  if amigos[i][0] or amigos[i][1]:
    print(i+1, end=' ')
    print(amigos[i][0] if amigos[i][2] else -1)
    