money = 1000-int(input())
coin_types = [500, 100, 50, 10, 5, 1]
answer = 0

for coin in coin_types:
    answer += money//coin
    money %= coin
print(answer)