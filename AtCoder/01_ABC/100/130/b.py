n, x = map(int, input().split())

l = list(map(int, input().split()))

sum = 0
count = 1

for i in range(len(l)) :
    sum += l[i]
    if sum <= x :
        count +=1

print(count)