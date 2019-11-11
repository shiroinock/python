n = int(input())

ans = 0

for i in range(n) :
    digit, unit = map(str, input().split())
    if unit == 'JPY' :
        ans += float(digit)
    else :
        ans += float(digit) * 380000

print(ans)