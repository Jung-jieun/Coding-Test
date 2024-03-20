n = int(input())
for i in range(n):
    money = int(input())
    for coin in [25,10,5,1]:
        print(money//coin, end=' ')
        money %= coin
        