n = input()

gu = [int(e) for e in input().split()]

gu.sort()

gunew = gu[0]

for i in gu :
    gunew = (gunew + i) / 2

print(gunew)