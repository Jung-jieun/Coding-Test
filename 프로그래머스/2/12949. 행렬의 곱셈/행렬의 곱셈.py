def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)): # arr1's row
        for j in range(len(arr2[0])): # arr2's col
            for k in range(len(arr1[0])): # arr1's col 
                answer[i][j] += arr1[i][k]*arr2[k][j]
    
    return answer