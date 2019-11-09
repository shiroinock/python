n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_dif = 0
tmp = 0
count_mns = 0
count_pls = 0

for i in range(n) :
    tmp = a[i] - b[i]
    sum_dif += tmp
    if tmp > 0 :
        count_pls += 1
    if tmp < 0 :
        count_mns += 1

if sum_dif >= 0 and count_pls >= count_mns :
    print('Yes')
else :
    print('No')