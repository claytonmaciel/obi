
consumo = int(input())
dist = int(input())
restante = int(input())

x = dist / consumo

resp = x - restante

if resp < 0:
    print(0.0)
else:
    print(round(resp, 1))
