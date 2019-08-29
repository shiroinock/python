#!/usr/bin/python3
n = int(input('数> '))
fac = 1
for i in range(1,n+1) :
    fac *= i
print(str(n)+'! =',fac,sep=' ')

# 1以上の整数を入力し、その数までのべき乗を計算するプログラムを作成せよ。