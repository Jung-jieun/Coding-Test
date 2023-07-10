def solution(money):
    answer = []
    coffee = money//5500
    rest = money%5500
    answer = [coffee, rest]
    return answer