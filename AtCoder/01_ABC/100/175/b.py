N = int(input())

L = list(map(int, input().split()))

L.sort()

ans = 0

if N >= 3 :
    for i in range(0, N - 1) :
        for j in range(1, N - 1 - i) :
            for k in range(2, N - i):
                if L[i] < L[i+j] < L[i+k] and L[i] + L[i+j] > L[i+k]:
                    ans += 1

print(ans)