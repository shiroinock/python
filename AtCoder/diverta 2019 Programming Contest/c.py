n = int(input())

b = 0
a = 0
ab = 0
ex = 0

for i in range(n) :
    tmp = input()
    ab += tmp.count('AB')
    if tmp[0] == 'B' :
        b += 1
    if tmp[-1] == 'A' :
        a += 1
    if tmp[0] == 'B' and tmp[-1] == 'A' :
        ex += 1

if max(a, b) > ex or ex == 0 :
    print(ab + min(a, b))
else :
    print(ab + min(a, b) - 1)