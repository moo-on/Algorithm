# "10 5 2"체력 공격력 방어력	["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"] 경험치 체력 공격력 방어력
import math


def solution(character, monsters):
    answer = ''
    character = character.split()
    play_HP = int(character[0])
    play_damage = int(character[1])
    play_defence = int(character[2])

    check_lst = []

    for monster in monsters:
        monster = monster.split()
        monster_name = monster[0]
        monster_experience, monster_HP, monster_damage, monster_defence = int(monster[1]), int(monster[2]), int(
            monster[3]), int(monster[4])

        time_damage = play_damage - monster_defence
        if time_damage <= 0: continue  # 사냥 못하는 경우

        total_time = math.ceil(monster_HP / time_damage)
        if (monster_damage - play_defence) * (total_time - 1) >= play_HP: continue  # player먼저 죽는 경우

        per_experience = monster_experience / total_time  # 1초당 얻는 경험치
        check_lst.append([monster_name, per_experience, monster_experience])  # 이름 초당경험치 잡앗을때 경험치

    check_lst.sort(key=lambda x: (-x[1], -x[2]))
    return check_lst[0][0]


print(solution("10 5 2", ["Knight 3 10 10 3", "Wizard 5 10 15 1", "Beginner 1 1 15 1"]))

# 100	200	[[0, 5], [1500, 3], [3000, 1]]	4100
# 49	200	[[0, 5], [1500, 3], [1501, 1]]	1800
# 11	1000	[[0, 5], [100, 4], [200, 3]]	2700

import math


def solution(time, gold, upgrade):
    answer = -1
    cnt = 0
    money = 0
    check_lst = []
    for i, state in enumerate(upgrade):
        if i < len(upgrade) - 1 and money > upgrade[i + 1][0]:
            money -= upgrade[i+1][0]
            continue
        expense = state[0]
        per_time = state[1]

        total_gold = (time // per_time) * gold + money
        check_lst.append(total_gold)
        print(check_lst)
        # 다음 단계 없으면 종료
        if i == len(upgrade) - 1: continue

        # 다음비용
        next_expense = upgrade[i + 1][0]

        # 업글레이드에 필요한 골드 개수
        need_gold = math.ceil(next_expense / gold)

        # 필요한 골드를 모으기까지 필요한 시간
        need_time = need_gold * per_time

        # 남은 돈과 시간
        money += need_gold * gold - next_expense
        time -= need_time

    return max(check_lst)


# print(solution(100, 200, [[0, 5], [1500, 3], [3000, 1]]))  # 시간, 금광석 가치, 업그레이드 비용
# print(solution(49,	200,	[[0, 5], [1500, 3], [1501, 1]]))
print(solution(11, 1000, [[0, 5], [100, 4], [200, 3]]))

# ["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"]	[1, 2, 4]	[2, 3]	4
# ["KKKK", "KKKK", "KKKK", "FGHI"]	[2, 3]	[2]	2
# ["KKK", "KKK", "KKK"]	[2]	[2]	1


def solution(cakes, cut_rows, cut_columns):
    answer = []
    temp_lst = []
    prev_row = 0
    for row in cut_rows:
        cake = cakes[prev_row:row]


        prev_column = 0
        for column in cut_columns:
            temp = []
            for e in cake:
                temp.append(e[prev_column:column])
            prev_column = column
            check = "".join(temp)
            temp_lst.append(len(set(list(check))))

        temp = []
        for e in cake:
            temp.append(e[prev_column:])

        check = "".join(temp)
        temp_lst.append(len(set(list(check))))

        prev_row = row

    cake = cakes[prev_row:]

    prev_column = 0
    for column in cut_columns:
        temp = []
        for e in cake:
            temp.append(e[prev_column:column])
        prev_column = column
        check = "".join(temp)
        temp_lst.append(len(set(list(check))))

    temp = []
    for e in cake:
        temp.append(e[prev_column:])

    check = "".join(temp)
    temp_lst.append(len(set(list(check))))

    return max(temp_lst)


print(solution(["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"], [1, 2, 4], [2, 3]))
