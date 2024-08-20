def solution(want, number, discount):
    answer = 0
    item = {}
    
    for i in range(len(want)):
        item[want[i]] = number[i]
        
    for j in range(len(discount)-9):
        item_copy = item.copy()
        for k in range(j,j+10):
            if discount[k] in item_copy and item_copy[discount[k]]!=0:
                item_copy[discount[k]] -= 1
            else:
                break
        if sum(item_copy.values())==0:
            answer += 1
    return answer