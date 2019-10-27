q, h, s, d = map(int, input().split())
n = int(input())

twoL = [q * 8, h * 4, s * 2, d]
twoL.sort()

if n % 2 == 0 :
    print(twoL[0] * (n // 2))
else :
    L = [q * 4, h * 2, s]
    L.sort()
    print(twoL[0] * (n // 2) + L[0])