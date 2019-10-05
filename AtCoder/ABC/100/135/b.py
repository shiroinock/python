n = int(input())

args = [int(e) for e in input().split()]

count = 0

for i in range(0, n) :
    if args[i] != i + 1 :
        count += 1

if count == 2 :
    print("YES")
elif count == 0 :
    print("YES")
else :
    print("NO")