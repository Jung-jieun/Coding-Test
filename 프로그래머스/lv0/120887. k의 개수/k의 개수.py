def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        if str(k) == str(num):
            answer += 1
        elif str(k) in str(num):
            for l in range(len(str(num))):
                if str(num)[l] == str(k):
                    answer += 1
    return answer