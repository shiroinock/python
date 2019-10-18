N, K = map(int, input().split())

H = [int(h) for h in input().split()]

count = 0

for i in range(0, N) :
    if H[i] >= K :
        count += 1

print(count)