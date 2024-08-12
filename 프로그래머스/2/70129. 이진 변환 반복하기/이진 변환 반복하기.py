def solution(s):
    time = 0
    zero_count = 0
    
    while True:
        if s=="1":
            break
        
        zero_count += s.count("0")
        s = s.replace("0", '')
        time += 1
        s = bin(len(s))[2:]
        
    return [time, zero_count]