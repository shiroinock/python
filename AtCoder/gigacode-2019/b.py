n, x, y, z = map(int, input().split())

count = 0

for i in range(n) :
    a, b = map(int, input().split())
    if a >= x and b >= y and (a + b) >= z :
        count += 1

print(count)