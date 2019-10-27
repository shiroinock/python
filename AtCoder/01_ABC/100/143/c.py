n = int(input())
s = list(input())

digit = 1

while digit < len(s) :
    if s[digit] == s[digit - 1] :
        s.pop(digit)
    else :
        digit += 1

print(len(s))