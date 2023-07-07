def solution(array):
    count_n = dict()
    for num in list(set(array)):
        cnt = array.count(num)
        if cnt in count_n.keys():
            count_n[array.count(num)].append(num)
        else:
            count_n[array.count(num)]=[num]
    max_n = count_n[max(count_n.keys())]
    if len(max_n) == 1:
        return max_n[0]
    else:
        return -1