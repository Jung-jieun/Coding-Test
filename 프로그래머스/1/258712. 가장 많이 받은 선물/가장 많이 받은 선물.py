def solution(friends, gifts):
    answer = [0]*len(friends)
    report = {}
    
    for name in friends:
        if name not in report:
            report[name] = [0]*len(friends)
    
    gift_index = {}
    for name in friends:
        if name not in gift_index:
            gift_index[name] = 0
            
    for gift in gifts:
        give, receive = gift.split()
        report[give][friends.index(receive)] += 1
        gift_index[give] += 1
        gift_index[receive] -= 1
    
    for i in friends:
        for j in friends:
            if i==j:
                break
            idx_1 = friends.index(i)
            idx_2 = friends.index(j)
            point_1 = report[i][idx_2] # muzi
            point_2 = report[j][idx_1] # frodo
            if point_1 > point_2:
                answer[friends.index(i)] += 1
            elif point_1 < point_2:
                answer[friends.index(j)] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    answer[friends.index(i)] += 1
                elif gift_index[i] < gift_index[j]:
                    answer[friends.index(j)] += 1
                    
    return max(answer)