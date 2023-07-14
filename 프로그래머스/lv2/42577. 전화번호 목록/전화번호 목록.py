def solution(phone_book):
    
    phone_book.sort()
    for idx, word in enumerate(phone_book):
        if idx != len(phone_book) - 1:
            word2 = phone_book[idx + 1]
            if word == word2[: len(word)]:
                return False  
    return True