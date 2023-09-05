def solution(n, arr1, arr2):
    num1 = []
    num2 = []
    result = []
    
    for i in range(0,n):
        num1.append(bin(arr1[i])[2:])
        num2.append(bin(arr2[i])[2:])
        num1[i] = ('0'*(n-len(num1[i]))) + num1[i]
        num2[i] = ('0'*(n-len(num2[i]))) + num2[i]
        
        answer = ''
        
        for j in range(0,n):
            if num1[i][j]=='1' or num2[i][j]=='1':
                answer += '#'
            elif num1[i][j]=='0' and num2[i][j]=='0':
                answer += ' '
        result.append(answer)
    return result