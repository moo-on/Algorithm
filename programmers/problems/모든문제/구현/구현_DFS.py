# [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]	22

def solution(dice):
    answer = 0
    set_lst = [set(l) for l in dice]

    for n in range(1, 10000):
        # 숫자 하나에 주사위 몇개 가능 한지 넣은 리스트
        check_lst = [[] for j in range(len(dice))]

        # 숫자를 하나씩 체크해보기 위한 리스트
        str_lst = list(map(int, list(str(n))))

        # 숫자를 하나 씩 주사위의 숫자랑 비교
        for i_1, e in enumerate(str_lst):
            for i_2, l in enumerate(set_lst):
                if e in l: check_lst[i_1].append(i_2)

        # 숫자에 몇개의 주사위가 맵핑 되어있는지 확인
        temp = set()
        for l in check_lst:
            for e in l:
                temp.add(e)
        # 맵핑된 숫자보다 작다면 해당 숫자 반환
        if len(temp)<len(str_lst):
            return n
    return 0

print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))
print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))