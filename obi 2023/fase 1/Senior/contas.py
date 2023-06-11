#Elnatan

v = int(input())
a = int(input())
f = int(input())
p = int(input())
l = [a,f,p]
l.sort()
c = 0
for i in l:
    if v >= i:
        v -= i
        c += 1
print(c)