def solution(age):
    answer = ''
    for i in str(age):
        alphabet = 'abcdefghij'
        answer += alphabet[int(i)]
    return answer