#!/usr/bin/python3
a = int(input('数1> '))
b = int(input('数2> '))
c = int(input('数3> '))
# 戦略。aを一番小さくし、次にbを決める。
if a > b :
    temp = a
    a = b
    b = temp
if a > c :
    temp = a
    a = c
    c = temp
#
# a が最小。
#
if b > c :
    temp = b
    b = c
    c = temp
print(a,b,c,sep=' ')

# ３つの数を入力し、数を昇順に並べ替えてから出力するプログラムを作成してください。