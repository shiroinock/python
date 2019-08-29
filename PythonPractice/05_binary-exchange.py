#!/usr/bin/python3
num = int(input('10進数> '))
first = num
# いろいろな方法あり。
b128 = num // 2**7
num = num % 2**7
b064 = num // 2**6
num = num % 2**6
b032 = num // 2**5
num = num % 2**5
b016 = num // 2**4
num = num % 2**4
b008 = num // 2**3
num = num % 2**3
b004 = num // 2**2
num = num % 2**2
b002 = num // 2
num = num % 2
binary = str(b128)+str(b064)+str(b032)+str(b016)+str(b008)+str(b004)+str(b002)+str(num)
print(first,'=',binary,sep=' ')

# 255以下の10進数を入力して、それを８桁の２進数で表示するプログラムを書きなさい。