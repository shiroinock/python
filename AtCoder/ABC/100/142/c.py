N = int(input())

A = [int(a) for a in input().split()]

Ans = [0] * N

for i in range(0, N) :
    Ans[A[i] - 1] = i + 1

print(' '.join(map(str,Ans)))