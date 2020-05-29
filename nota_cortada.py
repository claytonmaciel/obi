B = int(input())
T = int(input())
Area_total = 70 * 160
Area_felix = ((B+T)*70)/2
Area_Marzia = Area_total - Area_felix
if Area_felix > Area_Marzia:
    print(1)
elif Area_felix < Area_Marzia:
    print(2)
else:
    print(0)