pontos = [int(input()) for _ in range(5)]
set_pontos = sorted(set(pontos), reverse=True)

if len(set_pontos) >= 2:
    primeiro, segundo, *_ = set_pontos
    print(pontos.count(primeiro), pontos.count(segundo))

else:
    print(5, 0)