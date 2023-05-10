def solution(array):
    array_sort = sorted(array)
    if len(array_sort)>3:
        answer = array_sort[len(array_sort)//2]
    elif len(array_sort)==1:
        answer = array_sort[0]
    else:
        answer = array_sort[1]
    return answer