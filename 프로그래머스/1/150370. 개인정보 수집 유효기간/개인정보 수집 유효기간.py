def solution(today, terms, privacies):
    dictionary = {}
    answer = []
    today_list = list(map(int,today.split('.')))
    
    # 약관 종류와 개월 수 딕셔너리로 저장
    for term in terms:
        n, m = term.split()
        dictionary[n] = int(m)*28 # 일수
        
    for p in range(len(privacies)):
        date, s = privacies[p].split()
        collection_list = list(map(int, date.split('.')))
        year = (today_list[0] - collection_list[0])*336
        month = (today_list[1] - collection_list[1])*28
        day = today_list[2] - collection_list[2]
        total = year+month+day
        if dictionary[s] <= total:
            answer.append(p+1)
    return answer