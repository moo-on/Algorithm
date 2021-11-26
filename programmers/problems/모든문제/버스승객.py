#
#
#
#
#
#
#
#
# case1 = 1	1	5	["08:00", "08:01", "08:02", "08:03"]

def change_time(s):
    lst = s.split(":")
    total = int(lst[0]) * 60 + int(lst[1])
    return total


def change_str(n):
    h, m = divmod(n, 60)

    if len(str(h)) == 1:
        h = ''.join(['0', str(h)])
    if len(str(m)) == 1:
        m = ''.join(['0', str(m)])
    return ':'.join([h, m])


def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    bus_arrive = [540 + i * t for i in range(n)]

    cnt = 0
    for i, time in enumerate(timetable):
        if not bus_arrive:  # 버스가 없는데 사람이 남았다면
            last = i
            break

        if change_time(time) <= bus_arrive[0]:  # 버스 시간 전에 사람이 와있다면
            cnt += 1
        elif change_time(time) > bus_arrive[0]:  # 버스 도착 시간 보다 사람이 늦는다면 버스 출발 후, 사람 한 명 대기
            bus_arrive.popleft()
            cnt = 1

        if cnt == m:  # 사람이 꽉 찼다면 출발
            bus_arrive.popleft()
            cnt = 0
    else: #  반복문이 정상적으로 돌아가 사람을 전부 태우고 버스가 없다면
        if not bus_arrive:
            last = len(timetable) -1


    # 버스가 남아있다면 마지막 버스 타고 가기
    if bus_arrive:
        return change_str(bus_arrive[-1])
    # 버스와 사람 수가 딱 맞는다면 마지막 사람 앞에 타기
    if not bus_arrive and i == len(timetable) - 1:
        return change_str(change_time(timetable[-1]) - 1)

    return answer


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
