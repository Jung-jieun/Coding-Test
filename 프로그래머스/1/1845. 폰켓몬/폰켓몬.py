def solution(nums):
    answer = 0
    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
            
    if len(nums)//2<=len(freq):
        return len(nums)//2
    else:
        return len(freq)