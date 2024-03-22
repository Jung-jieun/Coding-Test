from collections import deque
def solution(arr):
    q = deque()
    for num in arr:
        if num not in q or num != q[-1]:
            q.append(num)
    return list(q)