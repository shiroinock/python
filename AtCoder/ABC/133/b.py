n, d = map(int,input().split())

a = 0
X = []

while a < n :
    X.append(input().split())
    a += 1

i = 0
j = 0
p = 0
wa = 0
count = 0

while i < n :
    p = 1
    while i + p < n :
        wa = 0
        j = 0
        while j < d :
            wa += pow(int(X[i][j]) - int(X[i + p][j]), 2)
            j += 1
        p += 1
        if (wa ** .5).is_integer() :
            count += 1
    i += 1

print(count)