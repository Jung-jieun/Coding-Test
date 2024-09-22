from itertools import permutations
def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers)+1):
        p = permutations(numbers, i)
        for j in p:
            num = int(''.join(j))
            
            if num > 1:
                is_prime = True
                for k in range(2, int(num**0.5)+1):
                    if num%k==0:
                        is_prime = False
                        break
                
                if is_prime and num not in answer:
                    answer.append(num)
    
    return len(answer)