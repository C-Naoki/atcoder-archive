def f(x):
  return x ** 2 + 2 * x + 3


if __name__ == "__main__":
  t = int(input())
  print(f(f(f(t) + t) + f(f(t))))
