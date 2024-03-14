def solution(s):
    count = 0
    for i in s:
        if i=='(':
            count += 1
        else :
            if count == 0:
                return False
            count -= 1
    if count==0:
        return True
    else:
        return False