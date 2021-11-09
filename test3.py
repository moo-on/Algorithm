# [2, 1, 3, 1, 2, 1]	[0, 1, 2]
# [3, 3, 3, 3, 3, 3]	[6, 6, 0]


def solution(arr):
    answer = []
    cnt_dict = {1: 0, 2: 0, 3: 0}

    #  원소 개수 카운트
    for e in arr:
        cnt_dict[e] += 1

    #  원소 1, 2, 3의 순서대로 정렬
    cnt_dict = dict(sorted(cnt_dict.items()))

    #  원소 중 최댓값 추출
    MAX = max(cnt_dict.values())

    #  추가로 필요한 원소 개수 카운트
    for value in cnt_dict.values():
        answer.append(MAX - value)

    return answer


print(solution([2, 1, 3, 1, 2, 1]))
print(solution([3, 3, 3, 3, 3, 3]))


#  ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]	"02:20"

def solution(log):
    total = 0

    #  시작과 끝 시간 step 맞춰주기
    for i in range(0, len(log), 2):
        #  시간, 분 나눠주기
        start = list(map(int, log[i].split(":")))
        stop = list(map(int, log[i + 1].split(":")))
        #  분으로 환산해서 처리
        time = (stop[0] * 60 + stop[1]) - (start[0] * 60 + start[1])

        #  조건 처리
        if time < 5:
            continue
        if time >= 105:
            time = 105

        total += time

    #  조건에 맞게 변환
    share, division = divmod(total, 60)

    if len(str(share)) > 1:
        answer = ''.join([str(share), ":", str(division)])
    else:
        answer = ''.join(["0",str(share), ":", str(division)])

    return answer


print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))

# ["r 10", "a 23", "t 124", "k 9"]
# ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
# ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]	1161

from collections import defaultdict


def translation(string, dict):
    total = 0
    for e in list(string):
        total += dict[e]
    return total


def solution(ings, menus, sales):
    ings_dict = {}
    for ing in ings:
        ing = ing.split()
        name, price = ing[0], ing[1]
        ings_dict[name] = int(price)

    menu_dict = {}
    for menu in menus:
        menu = menu.split()
        name, ing, sell_price = menu[0], menu[1], int(menu[2])

        raw_price = translation(ing, ings_dict)

        menu_dict[name] = sell_price - raw_price

    total = 0
    for sale in sales:
        sale = sale.split()
        name, cnt = sale[0], int(sale[1])
        total += menu_dict[name] * cnt

    return total


print(solution(["r 10", "a 23", "t 124", "k 9"],
               ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
                "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))

print(solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"]))


# "aaabbaaa"	[2,6]
# "wowwow"	[1,1,2,2]

def solution(s):
    answer = []
    rev_s = s[::-1]

    cnt = 0
    for i, e in enumerate(rev_s):
        if e == s[0]:
            cnt += 1
        else:
            break

    cnt_s = cnt
    discri = s[0]

    if cnt == len(s):
        return [cnt]

    if cnt == 0:
        cnt = -len(s)
        cnt_s = 0

    for e in s[:-cnt]:
        if discri == e:
            cnt_s += 1
        else:
            answer.append(cnt_s)
            cnt_s = 1
            discri = e

    answer.append(cnt_s)
    answer.sort()

    return answer


print(solution("aaabbaaa"))
print(solution("wowwow"))
print(solution("wowwob"))
print(solution("aaaaa"))
print(solution("aaaabb"))


# 3.5	[ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]	"홍콩"

# 월	1PM	6PM
# 금	9:30AM	6PM

def trans(string):
    time = int(string[:-2])
    if string[-2:] == "PM":
        time += 12
    return time


def solution(time, plans):
    answer = ''
    friday_start = 9.5
    friday_finish = 18
    friday_all = 8.5
    monday_start = 13
    monday_finish = 18
    monday_all = 5
    last_country = plans[0][0]

    for plan in plans:
        country, friday_trip_start, monday_trip_finish = plan[0], trans(plan[1]), trans(plan[2])

        #  금요일 퇴근 시각 전에 출발 한다면
        if friday_start <= friday_trip_start <= friday_finish:
            time -= friday_finish - friday_trip_start
        #  금요일 출근을 안한다면
        elif friday_trip_start < friday_start:
            time -= friday_all

        #  월요일 일과 시간 중 도착한다면
        if monday_start <= monday_trip_finish <= monday_finish:
            time -= monday_finish - monday_trip_finish
        #  월요일 출근을 안한다면
        elif monday_trip_finish > monday_finish:
            time -= monday_all

        if time < 0:
            return last_country
        else:
            last_country = country

    return answer


print(solution(3.5, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]))

# 3	4 [[8,2,13,14],[16,10,4,15],[17,11,12,6]]

def solution(rows, columns):
    answer = [[]]
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    matrix[0][0] = 1
    nx, ny = 0, 0
    cnt = 1
    zero_cnt = 1
    while True:
        #  최근 쓴 숫자 홀 수 일 때 다음 위치
        if matrix[nx][ny] % 2 == 1:
            if ny == columns - 1:
                ny = 0
            else:
                ny = ny + 1

        #  최근 쓴 숫자 짝 수 일 때 다음 위치
        elif matrix[nx][ny] % 2 == 0:
            if nx == rows - 1:
                nx = 0
            else:
                nx = nx + 1

        #  다음위치 반환 후, 작성 할 다음 숫자
        cnt += 1

        #  다음 위치가 0 이 아닐 경우, 똑같은 패턴을 가지게 될 경우 값 반환
        if matrix[nx][ny] != 0:
            if cnt % 2 == matrix[nx][ny] % 2:
                return matrix

        #  다음 위치가 0 일 경우, 빈 칸을 얼만큼 채웠는지 체크
        if matrix[nx][ny] == 0:
            zero_cnt += 1

        #  다음 좌표에 값을 작성
        matrix[nx][ny] = cnt

        #  빈 칸을 전부 채웠으면 값 반환
        if zero_cnt == rows * columns:
            return matrix

    return matrix


print(solution(3, 4))
print(solution(3, 3))
print(solution(10, 119))
