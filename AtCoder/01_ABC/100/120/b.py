a, b, k = map(int, input().split())

# ユークリッドの互除法
# a が最大公約数になっている
while b:
    a, b = b, a % b

a_divisors = []

for i in range(1, int(a ** 0.5) + 1) :
    if a % i == 0 :
        a_divisors.append(i)
        if a // i != i :
            a_divisors.append(a // i)

a_divisors.sort()

print(a_divisors[len(a_divisors) - k])