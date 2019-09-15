import statistics

n = int(input())

p = list(map(int, input().split()))

count = 0

for i in range(1, n) :
    pi = p[i]
    if statistics.median(p[i-1:i+2]) == p[i] :
        count += 1

print(count)