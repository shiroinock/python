L, R, d = map(int, input().split())

if L%d == 0 :
    print(R//d - L//d + 1)
else :
    print(R//d - L//d)