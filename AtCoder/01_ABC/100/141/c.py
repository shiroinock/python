#1
n, k, q = map(int, input().split())

C = [0] * n

for a in range(q) :
    C[int(input())-1] += 1

for i in range(n) :
    minus = sum(C) - C[i]
    if minus < k :
        print('Yes')
    else :
        print('No')


#2
n, k, q = map(int, input().split())
S = []
A = []

for a in range(q) :
    A.append(int(input()))

for i in range(n) :
    S.append(int(k))
    if S[i] - len(A) + A.count(i+1) > 0 :
        print('Yes')
    else :
        print('No')



#どっちの回答も入力例はパスするけどTLEで弾かれるので悲しみ