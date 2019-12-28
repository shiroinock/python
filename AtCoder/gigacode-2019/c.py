d = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sum = 0
min_prc = 2000000001

for i in range(d) :
    a_sum += a[i]
    if a_sum >= b[i] :
        min_prc = min(min_prc, b[i])

if min_prc >= 2000000001 :
    print(-1)
else :
    print(min_prc)