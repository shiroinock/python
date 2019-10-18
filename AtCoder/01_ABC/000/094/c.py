n = int(input())

x_org = list(map(int, input().split()))

x = sorted(x_org)

mid = x[n // 2 - 1]
midr = x[n // 2]

for i in range(n) :
    if x_org[i] <= mid :
        print(midr)
    else :
        print(mid)