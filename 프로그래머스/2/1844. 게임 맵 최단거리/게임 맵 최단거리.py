from collections import deque
def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])
    board = [] 
    
    q = deque([(0,0,1)])
    while q:
        x, y, dist = q.popleft()
        
        if x==n-1 and y==m-1:
            return dist
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 새로운 좌표가 범위 안에 있고, 벽이 아니라면 이동
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]== 1:
                # 방문한 곳은 다시 방문하지 않도록 함
                maps[nx][ny] = 0
                q.append((nx,ny,dist+1))
    return -1