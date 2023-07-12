num1 = [int(input()) for x in range(10)]
num2 = [a%42 for a in num1]
print(len(set(num2)))