from collections import Counter
def solution(topping):
    answer = -1
    dic = Counter(topping)
    cnt = 0
    brother = set()
    
    for i in topping:
        dic[i] -= 1
        brother.add(i)
        
        if dic[i]==0:
            dic.pop(i)
            
        if len(brother) == len(dic):
            cnt += 1
    
    return cnt