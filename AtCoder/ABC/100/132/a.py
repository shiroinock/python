S = list(input())
s = set(S)

ans = 'Yes'

if len(s) != 2 :
    ans = 'No'
else :
    a, b = s
    if not S.count(a) == S.count(b) == 2 :
        ans = 'No'

print(ans)