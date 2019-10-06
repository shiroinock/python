C = list(map(int, input().split()))

C.sort()

if C[0] + C[1] == C[2] :
    print('Yes')
else :
    print('No')