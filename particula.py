#forma 1
num = int(input())
for i in range(6,9):
    n = ((num-i)/8)+1
    if int(n) == n:
        print(i-5)
        break

#forma 2
n = int(input())
if n % 8 == 6:
    print(1)
elif n % 8 == 7:
    print(2)
else:
    print(3)

#forma 3
num = int(input())
num -= 5
print(num%8)

#forma 4
print((int(input())-5)%8)