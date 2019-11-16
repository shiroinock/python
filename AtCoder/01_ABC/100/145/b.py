n = int(input())
s = list(input())

flag = 0

if n % 2 == 0 :
    for i in range(n // 2) :
        if s[i] != s[i + n // 2] :
            flag = 1
else :
    flag = 1

if flag == 1 :
    print('No')
else :
    print('Yes')