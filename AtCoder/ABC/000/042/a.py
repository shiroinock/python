S = list(map(int, input().split()))

S.sort()

if S[0] == 5 and S[1] == 5 and S[2] == 7 :
    print('YES')
else :
    print('NO')