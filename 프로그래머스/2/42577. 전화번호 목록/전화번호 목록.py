def solution(phone_book):
    hashdict = {}
    phone_book.sort()
    answer = []
    for i in phone_book:
        hashdict[hash(i)] = i
        answer.append(i)
        
    # "12" 와 "312"가 있으면 True로 출력해야 함
    for j in range(len(answer)-1):
        if answer[j]==answer[j+1][:len(answer[j])]:
            return False
    return True
