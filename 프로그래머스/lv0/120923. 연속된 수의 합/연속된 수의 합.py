def solution(num, total):
    med = total//num
    return [i for i in range(med-(num-1)//2, med+(num+2)//2)]