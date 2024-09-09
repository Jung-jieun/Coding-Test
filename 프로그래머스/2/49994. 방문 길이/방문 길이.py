def solution(dirs):
    answer = 0
    direction = {'U':(0,1), 'D':(0,-1), 'R':(1,0),'L':(-1,0)}
    x, y = 0, 0
    visited = set()
    visited.add((0,0))
    
    for i in range(len(dirs)):
        
        dx, dy = direction[dirs[i]]
        nx, ny = x+dx, y+dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 양방향 경로를 기록
            if ((x, y), (nx, ny)) not in visited:
                visited.add(((x, y), (nx, ny)))
                visited.add(((nx, ny), (x, y)))
                answer += 1
            
            # 좌표 갱신
            x, y = nx, ny
    
    return answer