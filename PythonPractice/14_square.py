#!/usr/bin/python3
n = int(input('数> '))
print(str(n)+':',end='') # 改行しない出力
for i in range(0,n) :
    print('■',end='')
print() # 改行だけ出力
# Python3による別解
print(str(n)+':'+('■'*n))

# 数字を入力し、入力した数だけ画面に■印を表示するプログラムを書きなさい。