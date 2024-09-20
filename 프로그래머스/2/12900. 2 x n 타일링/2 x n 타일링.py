def solution(n):
    row, col = 2, 1
    for i in range(3, n+1):
        row, col = (row+col)%1000000007, row 
    return row