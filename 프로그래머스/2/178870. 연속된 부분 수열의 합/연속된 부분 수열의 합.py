def solution(sequence, k):
    answer = [0, len(sequence)]
    l = r = 0
    num = sequence[0]
    
    while True:
        if num<k:
            r += 1
            if r==len(sequence):
                break
            num += sequence[r]
        else:
            if num==k:
                if r-l<answer[1]-answer[0]:
                    answer = [l, r]
            num -= sequence[l]
            l += 1
    return answer