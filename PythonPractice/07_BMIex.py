#!/usr/bin/python3
height = float(input('身長をm単位で入力して下さい> '))
weight = float(input('体重をkg単位で入力して下さい> '))
bmi = weight/height**2
print('BMI = ',bmi,sep=' ')
if bmi < 18.5 :
    print('あなたは「'+'痩せすぎ'+'」です。')
elif bmi >= 18.5 and bmi < 25.0 :
    print('あなたは「'+'標準'+'」です。')
elif bmi >= 25.0 and bmi < 30.0 :
    print('あなたは「'+'肥満'+'」です。')
else :
    print('あなたは「'+'高度肥満'+'」です。')

# 健康のために肥満度をチェックしてみましょう。
# 身長と体重を入力してあなたの肥満度（BMI＝体重(kg)÷身長(m)の二乗）を計算するプログラムを作成し、
# 判定基準に従って、18.5未満→やせ、18.5〜25未満→標準、25〜30未満→肥満、30以上→高度肥満
# という判定を返すプログラムを作りなさい。