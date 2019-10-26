meals = []
a = 0

for i in range(5) :
    meal = int(input())
    if meal % 10 == 0 :
        meals.append(meal)
    else :
        if 10 - (meal % 10) > a :
            a = 10 - (meal % 10)
        meals.append(meal + 10 - (meal % 10))

print(sum(meals) - a)