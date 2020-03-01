n = int(input())
abc = []
ans = 0

for i in range(5) :
    abc.append(int(input()))

minabc = min(abc)
ans += n//minabc
if n % minabc != 0:
    ans += 1
print(4 + ans)