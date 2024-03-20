def solution(phone_book):
    answer = True
    phone_book.sort()
    phone_num = dict.fromkeys(phone_book, 1)
    
    for numbers in phone_num:
        num = ""
        for number in numbers:
            num += number
            if num in phone_num and num != numbers:
                return False
    return True