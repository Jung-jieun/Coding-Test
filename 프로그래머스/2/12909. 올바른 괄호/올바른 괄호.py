def solution(s):
    stack = []
    # stack에 '('을 넣어 s의 ')'과 짝을 짓는다.
    for i in s:
        if i=='(':
            stack.append(i) # '(' 일 경우 stack에 저장
        else:
            # stack에서 가장 마지막에 추가된 '('과 ')'
            if not stack: # stack이 비었으면
                return False
            stack.pop() # 가장 마지막에 넣은 '('을 제거해 ')'과 짝을 지어줌
    if len(stack)==0:
        return True
    return False # 반복문을 돌고도 원소가 남으면 false