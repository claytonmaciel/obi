n = int(input())
chocolates = sorted([int(input()) for i in range(n)])
print(sum(chocolates[n//3:]))
