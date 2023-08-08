def solution(board):
    row = [0,1,1,1,0,-1,-1,-1]
    col = [-1,-1,0,1,1,1,0,-1]
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==1:
                boom.append((i,j))
                
    for x,y in boom:
        for k in range(8):
            nx = x + row[k]
            ny = y + col[k]
            if 0<= nx < len(board) and 0<= ny<len(board):
                board[nx][ny] = 1
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                answer += 1
    return answer