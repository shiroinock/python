n = int(input())

n_divisors = []

for i in range(1, int(n ** 0.5) + 1) :
    if n % i == 0 :
        n_divisors.append(i)
        if n // i != i :
            n_divisors.append(n // i)
        else :
            n_divisors.append(i)

len_nd = len(n_divisors)

print(n_divisors[len_nd - 1] + n_divisors[len_nd - 2] - 2)