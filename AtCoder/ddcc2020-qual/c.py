h, w, k = map(int, input().split())

s = []

for i in range(h) :
    s.append(list(input()))

tmp = 0
ichigoFlag = False

for i in range(h) :
    for j in range(w) :
        if s[i][j] == '#' :
            tmp += 1
            ichigoFlag = True
            s[i][j] = tmp
        elif ichigoFlag == True :
            s[i][j] = tmp
        else :
            s[i][j] = 0
    ichigoFlag = False

for i in range(h) :
    for j in range(w-1) :
        if s[i][w-2-j] == 0 :
            s[i][w-2-j] = s[i][w-1-j]

for i in range(1,h) :
    if s[i][0] == 0 :
        s[i] = s[i-1]

for i in range(h-1, -1, -1) :
    if s[i][0] == 0 :
        s[i] = s[i+1]

for i in range(h) :
    print(*s[i])