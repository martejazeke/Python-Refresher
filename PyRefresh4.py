numbers = [('num1', '2.20'), ('num2','1.10'), ('num3','4.5')]

numbers.sort(key = lambda x: float(x[1]), reverse=True)

print(numbers)