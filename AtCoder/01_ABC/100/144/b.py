n = int(input())

# 割り切れたら1
flag  = 0

for i in range(1, 10) :
    if n % i == 0 and n // i < 10 :
        flag = 1

if flag == 1 :
    print('Yes')
else :
    print('No')