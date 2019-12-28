h, w, k, v = map(int, input().split())

if h == 1 and w == 1 :
    a = int(input())

    if a + k <= v :
        print(1)
    else :
        print(0)