from itertools import permutations
import math
def solution(numbers):
    answer = 0
    num = [n for n in numbers]
    per = []
    for i in range(1,len(num)+1):
        per += list(permutations(num, i))
    new_nums = [int(''.join(j)) for j in per]
    
    # 중복제거
    result = []
    for k in new_nums:
        if k not in result:
            result.append(k)
    
    def is_prime(x):
        if x<2:
            return False
        for p in range(2, int(math.sqrt(x))+1):
            if x%p==0:
                return False
        return True
    
    for r in result:
        if is_prime(r):
            answer += 1
    return answer