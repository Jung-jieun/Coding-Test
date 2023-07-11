def solution(num_list):
    n = [num_list for i in range(len(num_list)) if num_list[i]%2==0]
    a = [num_list for i in range(len(num_list)) if num_list[i]%2==1]
    answer = [len(n), len(a)]
    return answer