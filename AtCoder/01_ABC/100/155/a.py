A, B, C = map(int, input().split())

isPoor = False

if A == B and A != C :
    isPoor = True

if B == C and B != A :
    isPoor = True

if C == A and C != B :
    isPoor = True

if isPoor :
    print('Yes')
else :
    print('No')