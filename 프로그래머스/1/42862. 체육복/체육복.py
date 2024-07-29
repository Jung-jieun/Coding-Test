def solution(n, lost, reserve):
    
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    _reserve.sort()
    _lost.sort()
    
    for r in _reserve:
        q  = r-1
        s = r+1
        if q in _lost:
            _lost.remove(q)
        elif s in _lost:
            _lost.remove(s)
            
    return n - len(_lost)