n, x =map(int, input().split())
s = str(input())

for i in range(n):
    if s[i] == "x":
        if x != 0:
            x -= 1
    else:
        x += 1

print(x)