#Elnatan

a, b = [int(x) for x in input().split()]
sa = [int(x) for x in input().split()]
sb = [int(x) for x in input().split()]

p = 0
r = 'N'

for i in sa:
    if sb[p] == i:
        p +=1
    if p+1 >b:
        r = 'S'
        break
print(r)