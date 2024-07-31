from itertools import combinations
def solution(nums):
    
    answer = 0
    num_combi = list(combinations(nums, 3))
    
    def is_prime(x):
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    
    for j in num_combi:
        num = sum(j)
        if is_prime(num):
            answer += 1
        
    return answer