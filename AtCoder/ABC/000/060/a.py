a, b, c = map(str, input().split())

a_last = a[len(a) - 1]
b_last = b[len(b) - 1]

if a_last == b[0] and b_last == c[0] :
    print('YES')
else :
    print('NO')