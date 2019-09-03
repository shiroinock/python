a, b = map(int, input().split())
wa = a + b
if wa % 2 == 0 :
    print(int(wa / 2))
else :
    print("IMPOSSIBLE")