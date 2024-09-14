def solution(order):
    cnt = 0
    idx = 1
    container = []
    
    while idx<len(order)+1:
        container.append(idx)
        while container and container[-1]==order[cnt]:
            cnt+=1
            container.pop()
        idx += 1
    return cnt