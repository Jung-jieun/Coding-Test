def solution(sizes):
    w = []
    h = []
    for i in sizes:
        w.append(max(i[0], i[1]))
        h.append(min(i[0], i[1]))
    w.sort()
    h.sort()
    return w[-1]*h[-1]