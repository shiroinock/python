x,y = map(int, input().split())

absx = abs(x)
absy = abs(y)

ans = abs(absx - absy)

if absx < absy :
    if x < 0 :
        ans += 1
    if y < 0 :
            ans += 1
elif absx > absy :
    if x > 0 :
        ans += 1
    if y > 0 :
            ans += 1
else :
    if x != y :
        ans =1

print(ans)