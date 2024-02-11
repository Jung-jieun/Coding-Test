def solution(nums):
    answer = 0
    result = []
    num = len(nums)//2
    set1 = list(set(nums))
    if len(set1)<num:
        return len(set1)
    else:
        return num