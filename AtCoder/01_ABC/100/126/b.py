s = input()

if 0 < int(s[:2]) < 13 :
    if 0 < int(s[2:]) < 13 :
        print('AMBIGUOUS')
    else :
        print('MMYY')
else :
    if 0 < int(s[2:]) < 13:
        print('YYMM')
    else :
        print('NA')