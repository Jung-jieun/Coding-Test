def solution(lottos, win_nums):
    answer = []
    agree = 0
    zero = 0
    # 일치:순위
    result = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for i in lottos:
        if i==0:
            zero += 1
    
    while win_nums:
        num = win_nums.pop()
        
        # 있으면
        if num in lottos:
            lottos.remove(num)
            agree += 1
    
    min_result = result[agree]
    agree += zero
    max_result = result[agree]
    
    return [max_result,min_result]