def solution(id_list, report, k):
    answer = [0]*len(id_list)
    user_id = {} # {신고당한 id : 횟수}
    report = list(set(report))
    
    for idx in id_list:
        if idx not in user_id:
            user_id[idx] = 0
    
    for r in report:
        user_id[r.split()[1]] += 1
    
    for r in report:
        if user_id[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    return answer