def solution():
    answer_lst = []

    def test():
        answer_lst.append(3)
        return

    test()

    print(answer_lst)
    return

solution()