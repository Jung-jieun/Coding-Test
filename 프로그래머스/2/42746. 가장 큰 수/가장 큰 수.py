def solution(numbers):
    
    num_str = [str(number) for number in numbers]
    num_str.sort(key=lambda num:num*3, reverse=True)
    
    return str(int(''.join(num_str)))