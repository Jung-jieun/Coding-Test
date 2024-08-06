def solution(wallpaper):
    answer = []
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                answer.append((i,j))
                
    for k in range(len(answer)):
        x.append(answer[k][0])
        y.append(answer[k][1])
    return [min(x), min(y), max(x)+1, max(y)+1]
        
    # return [lux, luy, rdx, rdy]