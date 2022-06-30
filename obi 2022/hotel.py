diaria = int(input())
aumento = int(input())
dia = int(input())

if dia == 1:
    valor_total = diaria * 31
elif dia <= 15:
    valor_total = (diaria + (aumento * (dia - 1))) * (32 - dia)
else:
    valor_total = (diaria + (aumento * 14)) * (32 - dia)

print(valor_total)