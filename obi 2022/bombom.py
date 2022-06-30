def pontuar(domin, cartas):
    pontos = {'A': 10, 'J': 11, 'Q': 12, 'K': 13}

    pontuação = 0
    for fig, nipe in cartas:
        pontuação += pontos[fig]

        if nipe == domin:
            pontuação += 4

    return pontuação


dominante = input()[1]
cartas = [input() for i in range(6)]

Luana = pontuar(dominante, cartas[:3])
Edu = pontuar(dominante, cartas[3:])

if Edu > Luana:
    print("Edu")

elif Luana > Edu:
    print('Luana')

else:
    print("empate")

