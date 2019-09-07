n = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]
C = [int(c) for c in input().split()]

point = 0
i = 0

while  i < n :
    point += B[A[i] - 1]
    if i > 0 and A[i-1] == A[i] - 1 :
        point += C[A[i-1]-1]
    i += 1

print(point)