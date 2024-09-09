from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0,0)])
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = True
    
    n = len(maps)
    m = len(maps[0])
    
    while queue:
        x, y = queue.popleft()
        
        if x==n-1 and y==m-1:
            answer = maps[x][y]
            return answer
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny]!=0 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y] +1 
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    answer = -1
    return answer