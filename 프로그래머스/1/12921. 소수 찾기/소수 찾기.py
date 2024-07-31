def solution(n):
    answer = 0
    nums = [i for i in range(2, n+1)]
    
    def is_prime(x):
        for n in range(2, int(x**0.5)+1):
            if x%n==0:
                return False
        return True
    
    for j in nums:
        if is_prime(j):
            answer += 1
    return answer