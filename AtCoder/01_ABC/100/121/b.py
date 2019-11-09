n, m, c = map(int, input().split())

b = list(map(int, input().split()))

count = 0

for i in range(n) :
    sum = c
    a = list(map(int, input().split()))
    for j in range(m) :
        sum += a[j] * b[j]
    if sum > 0 :
        count += 1

print(count)