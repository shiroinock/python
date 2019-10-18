n, q = map(int, input().split())

s = input()

count = [0] * n

for i in range(n) :
    if s[i-1] + s[i] == 'AC' :
        count[i] = count[i-1] + 1
    else :
        count[i] = count[i-1]

for j in range(0, q) :
    l, r = map(int, input().split())
    print(count[r-1] - count[l-1])