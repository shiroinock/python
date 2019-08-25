#フィボナッチ数列をいい感じに表示するやつ

def fib1(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib1(n - 1) + fib1(n - 2)

def fib2(n):
  n0, n1 = 0, 1
  for cnt in range(n):
    n0, n1 = n1, n0 + n1
  return n1

print('call fib1')
for x in range(10):
  print(f'{fib1(x)}, ', end='')
print()
print('call fib2')
for x in range(10):
  print(f'{fib2(x)}, ', end='')
print()