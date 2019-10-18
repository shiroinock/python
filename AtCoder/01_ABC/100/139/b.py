a, b = map(int, input().split())

if b == 1 :
    print(0)
else :
    count = 1

    kuchi = a

    while kuchi < b :
        count+=1

        kuchi = (a - 1) * count + 1
    else :
        print(count)

"""要求数１の時は例外処理だよね"""
"""もっといい書き方絶対ある"""