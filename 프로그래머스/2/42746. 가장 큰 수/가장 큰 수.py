def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers의 원소가 1000이하이기에 4자리를 반복해 정렬
    numbers.sort(key=lambda x:x*4, reverse=True) 
    answer = str(int(''.join(numbers)))
    # str(int())을 하지 않으면 0이 '0000'으로 출력됨
    return answer