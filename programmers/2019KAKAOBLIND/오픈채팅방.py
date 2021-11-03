from collections import defaultdict


def solution(records):
    answer = []
    id_dict = defaultdict(str)
    for i, e in enumerate(records):
        records[i] = e.split()

    # 1. 뒤에서 부터 아이디와 닉네임 저장하며 순회
    # 2. 이미 존재하는 아이디는 스킵
    # 3. Change, Enter 명령어에만 아이디 저장

    for record in reversed(records):
        if record[0] == "Leave":
            continue

        command, uid, nickname = record[0], record[1], record[2]

        if uid not in id_dict:
            id_dict[uid] = record[2]

    for record in records:
        command, uid = record[0], record[1]
        if command == "Enter":
            answer.append(id_dict[uid] + "님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(id_dict[uid] + "님이 나갔습니다.")

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid   4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
