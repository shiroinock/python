x = int(input())

if x == 1000 :
    print(1000)
else :
    beki = []
    for i in range(2, 10) :
        beki.append(int(x ** (1 / i)) ** i)

    print(max(beki))