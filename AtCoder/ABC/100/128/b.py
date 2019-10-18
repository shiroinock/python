n = int(input())

x = []

for i in range(n) :
    s, p = map(str, input().split())
    x.append((s, -int(p), i+1))

x.sort()

for i in range(n) :
    print(x[i][2])