n, c = (int(i) for i in input().split())

p0 = [i for i in range(1,n+1)] #p0 é paciente zero, assumo que todos são pacientes zero

for i in range(c):
    infectados = [int(j) for j in input().split()[2:]] #da entrada, eu pego somente os infectados por humanos
    for j in infectados: #removo da lista dos pacientes zero.
        p0.remove(j)

print('\n'.join(str(i) for i in sorted(p0))) #imprimo o(s) paciente(s) zero de forma ordenada