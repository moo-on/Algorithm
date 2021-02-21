def solution(phone_book):
    set_ = set()
    for L in phone_book:
        for j in range(len(L)-1):
            for i in range(len(L)-j):
                    set_.add(L[i:i+j+1])
                    print(L[i:i+j+1])
    for L in phone_book:
        if L in set_: return False
    return True

solution(['119', '97674223', '1195524421'])


