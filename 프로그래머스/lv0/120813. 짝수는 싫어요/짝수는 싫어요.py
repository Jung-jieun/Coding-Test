def solution(n):
    if n%2==0 :
        answer = [i for i in range(n) if  i %2 ==1]
    elif n%2==1:
        answer = [i for i in range(n+1) if i%2 ==1]
    return answer