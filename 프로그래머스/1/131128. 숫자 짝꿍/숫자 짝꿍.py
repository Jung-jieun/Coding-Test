from collections import deque, Counter
def solution(X, Y):
    X = deque(X)
    Y = Counter(Y)
    result = []
    
    while X:
        i = X.popleft()
        if Y[i]>0:
            Y[i] -= 1
            result.append(int(i))
    
    result.sort(reverse=True)
    
    if len(result)==0:
        return "-1"
    if result[0]==0:
        return "0"
    else:
        return ''.join(str(i) for i in result)
    
    return result
    