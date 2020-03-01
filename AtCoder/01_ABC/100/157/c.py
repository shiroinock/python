n, m = map(int, input().split())

listans = ["0"] * n
ans = 0

for i in range(m):
    s, c = map(str, input().split())
    if n > 1 and s == "1" and c == "0":
        ans = -1
    if listans[int(s)-1] != c:
        if listans[int(s)-1] == "0":
            listans[int(s)-1] = c
        else :
            ans = -1

if ans == 0:
    if n > 1 and listans[0] == "0":
        listans[0] = "1"
    ans = int("".join(listans))

print(ans)