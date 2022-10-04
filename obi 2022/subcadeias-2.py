def eh_palindroma(cadeia):
    for i in range(len(cadeia)):
        if cadeia[i] != cadeia[-i-1]:
            break
    else:
        return cadeia


def iterar_cadeia(cadeia, n):
    for c1 in range(n):
        for c2 in range(n):
            if eh_palindroma(cadeia[c1:c2+1]):
                yield len(cadeia[c1:c2+1])


N = int(input())
string = input()

print(max(iterar_cadeia(string, N)))
