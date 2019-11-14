n = int(input())

h = list(map(int, input().split()))

tmp = 0
ans = 0

for i in range(n) :
    if tmp <= h[i] :
        ans += h[i] - tmp
        tmp  = h[i]
    else :
        tmp = h[i]

print(ans)