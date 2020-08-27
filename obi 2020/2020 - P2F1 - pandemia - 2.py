N, M = [int(value) for value in input().split()]
I, R = [int(value) for value in input().split()]

restrictions = True

restrictions = False if 2>N and N>1000 else restrictions
restrictions = False if 2>M and M>1000 else restrictions
restrictions = False if 1>I and I>N else restrictions
restrictions = False if 1>R and R>M else restrictions

reunions = []
infected = {I}

for _ in range(M):
    reunions.append([int(value) for value in input().split()])
    restrictions = False if 1>reunions[-1][0] and reunions[-1][0]>N else restrictions
    reunions[-1].pop(0)
    restrictions = False if any(P<1 and N<P for P in reunions[-1]) else restrictions

if restrictions:
    for i in range (R-1, M):
        if any(person in infected for person in reunions[i]):
            infected.update(reunions[i])

    print(len(infected))
