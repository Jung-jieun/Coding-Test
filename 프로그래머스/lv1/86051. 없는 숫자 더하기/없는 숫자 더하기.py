def solution(numbers):
    set1 = set(numbers)
    set2 = set(i for i in range(0,10))
    num = set2 - set1
    return sum(num)