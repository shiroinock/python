N = int(input())

n = N%10

honList = [2, 4, 5, 7, 9]
ponList = [0, 1, 6, 8]

if n in honList:
    print('hon')
elif n in ponList:
    print('pon')
else :
    print('bon')