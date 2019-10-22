from bisect import bisect_left

n = int(input())
l = list(map(int, input().split()))

l.sort()
count = 0

for i in range(n - 2) :
    for j in range(i + 1, n - 1) :
        idx = bisect_left(l, l[i] + l[j])
        count += idx - (j + 1)

print(count)


'''
#愚直TLEver
n = int(input())
l = list(map(int, input().split()))

l.sort()
count = 0

for i in range(n) :
    for j in range(1, n - i) :
        for k in range(1, n - i - j) :
            if l[i] + l[i + j] >= l[i + j + k] :
                count += 1

print(count)
'''