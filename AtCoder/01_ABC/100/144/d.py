import math

a, b, x = map(int, input().split())

height = x / (a ** 2)

if height <= b / 2 :
   print(90 - math.degrees(math.atan((x * 2) / (a * b * b))))
else :
    print(math.degrees(math.atan((a * a * b - x) * 2 / (a ** 3) )))