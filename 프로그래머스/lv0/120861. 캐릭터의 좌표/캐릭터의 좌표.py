def solution(keyinput, board):
    result = [0,0]
    for i in keyinput:
        if i=="left":
            result[0] -=1
        elif i=="right":
            result[0] +=1
        elif i=="up":
            result[1] +=1
        else:
            result[1]-=1
        if abs(result[0]) > (board[0]//2):
        
            if result[0]>0:
            
                result[0] = (board[0]//2)
            
            else:
                result[0] = -1*(board[0]//2)
            
        if abs(result[1]) > board[1]//2:
            if result[1]>0:
                result[1] = board[1]//2
            else:
                result[1] = -1*(board[1]//2)
    return result