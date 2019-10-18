n, l = map(int, input().split())


pie = [l + i for i in range(n)]
pie_abs = [abs(pie[j]) for j in range(n)]

pie.pop(pie_abs.index(min(pie_abs)))

print(sum(pie))