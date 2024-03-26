def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack :
        return False
    else:
        return True