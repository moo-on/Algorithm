def solution(s):
    answer = []
    dict_ = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
             "eight": "8", "nine": "9"}
    temp = ""
    for e in s:
        if e.isdecimal():
            answer.append(e)
        else:
            temp += e
            if temp in dict_:
                answer.append(dict_[temp])
                temp = ""

    return int(''.join(answer))



