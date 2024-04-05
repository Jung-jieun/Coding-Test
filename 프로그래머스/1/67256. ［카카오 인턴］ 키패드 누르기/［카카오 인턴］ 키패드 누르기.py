def solution(numbers, hand):
    answer = ''
    
    # (x,y)
    keypad = {'*':(0,0), 0:(1,0), '#':(2,0),
             7 : (0,1), 8:(1,1), 9:(2,1),
             4:(0,2), 5:(1,2), 6:(2,2),
             1:(0,3), 2:(1,3), 3:(2,3)}
    
    left = keypad["*"]
    right = keypad["#"]
    
    for num in numbers:
        current = keypad[num]
        if num in [1,4,7]:
            answer +="L"
            left = current
        elif num in [3,6,9]:
            answer += "R"
            right = current
        else:
            distance_l = abs(left[0]-current[0]) + abs(left[1]-current[1])
            distance_r = abs(right[0]-current[0]) + abs(right[1]-current[1])
            
            if distance_l<distance_r:
                answer += "L"
                left = current
            elif distance_l>distance_r:
                answer += "R"
                right = current
            else:
                if hand=="left":
                    answer += "L"
                    left = current
                else:
                    answer += "R"
                    right = current
    return answer