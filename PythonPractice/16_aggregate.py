#!/usr/bin/python3
counter = 0
gokei = 0
data = int(input('データ入力(負の数で終了)> '))
while data >= 0 :
    counter += 1
    gokei += data
    data = int(input('データ入力(負の数で終了)> '))
heikin = gokei/counter
print('データ数:',counter,'合計:',gokei,'平均:',heikin)

# 数を次々と入力し、負の数が入力されるまで続け、負の数が入力されたら、
# それまでの数の合計と平均を求めるプログラムを書きなさい。