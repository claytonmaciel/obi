dias_total = 31

diaria = int(input())
aumento = int(input())
chegada = int(input()) - 1

if chegada == 0:
    print(31 * diaria)

elif chegada < 15:
    print((dias_total - chegada) * (diaria + chegada * aumento))

else:
    print((dias_total - chegada) * (diaria+14*aumento))
