def solution(balls, share):
    def my_factorial(n):
        if (n>1):
            return n*my_factorial(n-1)
        else:
            return 1
    answer = my_factorial(balls)/(my_factorial(balls-share)*my_factorial(share)) 
    return answer