n = int(input())
h = list(map(int, input().split()))

ans = 0
tmp = 0

for i in range(1, n) :
    if h[i] <= h[i - 1] :
        tmp += 1
    else :
        if tmp >= ans :
            ans = tmp
        tmp = 0


print(max(ans, tmp))