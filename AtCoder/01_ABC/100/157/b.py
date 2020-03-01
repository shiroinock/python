a = []

for i in range(3):
    a.append(list(map(int, input().split())))

n = int(input())

b = []

for i in range(n):
    b.append(int(input()))

ans = "No"
flag = 0

#yoko
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            flag += 1
    if flag == 3:
        ans = "Yes"
    flag = 0

#tate
for j in range(3):
    for i in range(3):
        if a[i][j] in b:
            flag += 1
    if flag == 3:
        ans = "Yes"
    flag = 0

#naname1
for i in range(3):
    for j in range(3):
        if i == j:
            if a[i][j] in b:
                flag += 1
        if flag == 3:
            ans = "Yes"
flag = 0

#naname2
for i in range(3):
    for j in range(3):
        if i + j == 2 :
            if a[i][j] in b:
                flag += 1
        if flag == 3:
            ans = "Yes"
flag = 0

print(ans)