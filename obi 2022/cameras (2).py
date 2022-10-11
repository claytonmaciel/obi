n, m, k = map(int, input().split())  # m = linha n = coluna

def norte(mat, coluna, linha):
    for l in range(m):
        if l <= linha - 1:
            mat[l][coluna-1] = 0


def sul(mat, coluna, linha):
    for l in range(m):
        if l >= linha - 1:
            mat[l][coluna-1] = 0


def leste(mat, coluna, linha):
    for c in range(n):
        if c >= coluna-1:
            mat[linha-1][c] = 0


def oeste(mat, coluna, linha):
    for c in range(n):
        if c <= coluna - 1:
            mat[linha - 1][c] = 0


matriz = [[-1 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    c, l, d = input().split()
    foo = {'N': norte, 'S': sul, 'O': oeste, 'L': leste}[d]
    foo(matriz, int(c), int(l))


pilha = [(0, 0)]
while pilha:
	x, y = pilha.pop()
	
	if matriz[x][y] == -1:
		matriz[x][y] = 1
		
		if x < m - 1:
			pilha.append(((x+1, y)))
		
		if y < n - 1:
			pilha.append((x, y+1))
		
		if x:
			pilha.append((x-1, y))
		
		if y:
			pilha.append((x, y-1))


if matriz[m-1][n-1] == 1:
	print("S")

else:
	print("N")