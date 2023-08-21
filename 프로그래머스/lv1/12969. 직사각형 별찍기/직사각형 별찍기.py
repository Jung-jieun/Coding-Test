a, b = map(int, input().strip().split(' '))
array = [['*' for j in range(a)] for i in range(b)]
for i in array:
    for j in i:
        print(j, end="")
    print()