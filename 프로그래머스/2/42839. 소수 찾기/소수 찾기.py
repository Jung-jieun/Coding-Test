from itertools import permutations
def solution(numbers):
    number = list(numbers)
    num = []
    
    for i in range(1, len(number)+1):
        for permutation in permutations(number,i):
            if int(''.join(permutation))==1 or int(''.join(permutation))==0:
                continue
            else:
                num.append(int(''.join(permutation)))
    
    num = list(set(num))
    answer = 0
    
    def is_prime(x):
        for k in range(2, x):
            if x%k==0:
                return False
        return True
        
    for j in num:
        if is_prime(j):
            answer += 1
    
    return answer
