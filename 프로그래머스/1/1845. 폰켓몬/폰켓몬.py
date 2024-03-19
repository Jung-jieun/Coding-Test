from itertools import permutations
def solution(nums):
    data = dict.fromkeys(set(nums), 0)
    for num in nums:
        data[num] += 1
        
    answer = min(len(data), len(nums)//2)
       
    return answer