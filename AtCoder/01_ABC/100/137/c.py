n = int(input())

dic = {}
count = 0

for i in range(n) :
    tmp = str.join('', sorted(list(input())))
    if tmp not in dic :
        dic[tmp] = 0
    else :
        dic[tmp] += 1
        count += dic[tmp]

print(count)