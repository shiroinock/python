#!/usr/bin/python3
import random
print('ジャンケンポン!')
yours = int(input('あなたは？(0:グー, 1:チョキ, 2:パー)> '))
comp = random.randint(0,2)
if comp == 0 : # グー
    compstr = 'わたしはグー。'
    if yours == 0 :
        yourstr = 'あなたもグー。'
        result = 'あいこです。'
    elif yours == 1 :
        yourstr = 'あなたはチョキ。'
        result = 'あなたの負けです。'
    else :
        yourstr = 'あなたはパー。'
        result = 'あなたの勝ちです。'
elif comp == 1 : # チョキ
    compstr = 'わたしはチョキ。'
    if yours == 0 :
        yourstr = 'あなたはグー。'
        result = 'あなたの勝ちです。'
    elif yours == 1 :
        yourstr = 'あなたもチョキ。'
        result = 'あいこです。'
    else :
        yourstr = 'あなたはパー。'
        result = 'あなたの負けです。'
else : # パー
    compstr = 'わたしはパー。'
    if yours == 0 :
        yourstr = 'あなたはグー。'
        result = 'あなたの負けです。'
    elif yours == 1 :
        yourstr = 'あなたはチョキ。'
        result = 'あなたの勝ちです。'
    else :
        yourstr = 'あなたもパー。'
        result = 'あいこです。'
print(compstr+yourstr+result)

# 計算機とジャンケンをするプログラムを書きましょう。
# グー、チョキ、パーをそれぞれ0,1,2の整数で表すとします。
# あなたの出す手を整数で入力し、勝負するようにします。
# コンピュータの出す手は乱数（同じ確率ででたらめに数を自動的に生成する仕組み）を使って作り出します。
# 具体的には、random.randint(最小値, 最大値)という式を使うと
# 自動的に最小値から最大値までのでたらめな整数を作ってくれます。
# (プログラムの始めに、'import random'の宣言が必要)
#  comp=random.randint(0,2)
# こうすると、このcompに0か1か2の整数がでたらめに代入されます。
# 入力したあなたの手とこのcompを比較して、ジャンケンの勝負を判定するプログラムを作りなさい。