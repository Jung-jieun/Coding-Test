def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def dfs(a, b, l):
        start = arr[a][b]
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[i][j]!=start:
                    l = l//2
                    dfs(a,b,l)
                    dfs(a+l,b,l)
                    dfs(a,b+l,l)
                    dfs(a+l,b+l,l)
                    return
        answer[start] += 1
    dfs(0,0,length)
    return answer