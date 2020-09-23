def main():
    f = input()
    s = input()

    if len(s) == len(f):
        for i in set(s):
            if i != '*':
                if not s.count(i) <= f.count(i):
                    return None
        print('S')
        return True

if main() is None:
    print('N')
else:
    print('S')