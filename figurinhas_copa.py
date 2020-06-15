#=============================#
# Questão Figurinhas da Copa  #
#=============================#

n, c, m = [int(i) for i in input().split()]
fcar = [int(i) for i in input().split()]
fcom = [int(i) for i in input().split()]

fcarr = 0
for i in range(c):
    if fcar[i] not in fcom:
        fcarr += 1
print(fcarr)
