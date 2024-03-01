def solution(a, b):
    # a=2, b=29면 넘어가기.
    # 31일 : 1,3,5,7,8,10,12
    # 30일 : 4,6,9,11
    
    day = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30,
          7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    days =['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    
    for month in range(1,a):
        b += day[month]
        
    return days[b%7-1]

        