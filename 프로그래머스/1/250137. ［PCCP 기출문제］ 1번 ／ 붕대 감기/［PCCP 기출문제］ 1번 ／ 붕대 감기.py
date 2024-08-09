def solution(bandage, health, attacks):
    answer = health
    time = 0
    success = 0 # 연속 성공 
    
    while len(attacks)>0:
        if time == attacks[0][0]:
            answer -= attacks[0][1]
            success = 0
            attacks.pop(0)
            if answer <= 0:
                answer = -1
                break
        else:
             answer += bandage[1]
             if answer > health:
                answer = health
             success += 1
             if success == bandage[0]:
                answer += bandage[2]
                if answer > health :
                    answer = health
                success = 0
        time += 1
    return answer