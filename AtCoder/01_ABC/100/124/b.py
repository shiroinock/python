n = int(input())
h = list(map(int, input().split()))

tmp_max = h[0]
count = 1

for i in range(1, len(h)) :
    if tmp_max <= h[i] :
        count += 1
        tmp_max =  h[i]

print(count)