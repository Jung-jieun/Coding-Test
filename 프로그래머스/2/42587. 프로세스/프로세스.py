def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while queue:
        process = queue.pop(0)
        if any(process[1]<q[1] for q in queue):
            queue.append(process)
        else:
            answer += 1
            if process[0] == location:
                return answer
