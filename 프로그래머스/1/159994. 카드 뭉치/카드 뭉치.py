def solution(cards1, cards2, goal):
    answer = 'Yes'
    # goal 요소와 cards1, cards2랑 비교하기
    for i in goal:
        if cards1 and cards1[0]==i: # cards1이 비어있지 않아야 함!
            del cards1[0] # 한 번 사용한 카드는 다시 사용 불가
        elif cards2 and cards2[0]==i:
            del cards2[0]
        else:
            return 'No'
    return answer