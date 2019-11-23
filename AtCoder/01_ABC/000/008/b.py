n = int(input())

dic = {}

for i in range(n) :
    tmp = input()

    if tmp in dic :
        dic[tmp] += 1
    else :
        dic[tmp] = 1

namae, hyou = max(dic.items(), key=lambda x: x[1])

print(namae)