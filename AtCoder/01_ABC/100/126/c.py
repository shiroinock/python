n, k = map(int, input().split())

exp = 0
tmp = 0
point= 0

for i in range(1, n + 1) :
    point = i
    tmp = 1 / n
    while point < k :
        point *= 2
        tmp /= 2
    exp += tmp

print(exp)