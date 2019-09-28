a, b = map(int, input().split())


while b:
    a, b = b, a % b

# aが最大公約数になっている

def factorization(a):
    arr = []
    temp = a
    for i in range(2, int(-(-a**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([a, 1])

    return arr

soinsuu = len(factorization(a))

if soinsuu == 1 :
    print(1)
else :
    print(soinsuu + 1)