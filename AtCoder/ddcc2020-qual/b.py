n = int(input())

A = list(map(int, input().split()))

sum_A = sum(A)

A_wa = [0]
A_nokori = [sum_A]

for i in range(n) :
    A_wa.append(A_wa[i] + A[i])
    A_nokori.append(A_nokori[i] - A[i])

dif_A = []

for i in range(n) :
    dif_A.append(abs(A_nokori[i] - A_wa[i]))

print(min(dif_A))