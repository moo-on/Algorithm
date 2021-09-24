# 원소의 값 : 0~1000
case1 = [6, 10, 2]  # "6210"
case2 = [3, 30, 34, 5, 9]  # "9534330"
case3 = [1000, 999, 0, 0, 123]
case4 = [87, 878]
case5 = [89, 898]
case5 = [0, 0]
case6 = [9, 997, 99, 878, 87]
case7 = [10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
case8 = [412, 41]
case9 = [303, 30]


# 앞자리가 같은 문자들 전부 모아서 자릿수 맞춘 후 비교
def solution(numbers):
    answer = []
    lst = [[] for _ in range(10)]
    cnt_1000 = 0
    cnt_0 = 0
    # lst 안에 앞자리가 같은 문자들 모아주기
    for number in numbers:
        #예외처리
        if number == 1000:
            cnt_1000 += 1
            continue
        if number == 0:
            cnt_0 +=1
            continue
        start = int(str(number)[0])  # 원소의 앞자리 번호
        end = int(str(number)[-1])  # 원소의 끝자리
        if number>=100: # 3자리
            lst[start].append([str(number), number])  # [기존 넘버, 비교용 자릿수 맞춰 준 넘버]
        elif number>=10: # 2자리
            if end>=start:
                comparison_number = int(str(number).ljust(3, str(start))) + 0.1
            else:
                comparison_number = int(str(number).ljust(3, str(start))) - 0.1
            lst[start].append([str(number), comparison_number])  # [기존 넘버, 비교용 자릿수 맞춰 준 넘버]
        else: # 1자리
            lst[start].append([str(number), int(str(number).ljust(3, str(start)))])



    lst.reverse()  # lst 배열을 뒤집어서 앞자리가 9부터 0까지 순서로 순회하기
    for l in lst:
        l.sort(key=lambda x: x[1], reverse=True)  # 9부터 순서 맞춰주기
    # 순서가 맞춰졌으니, 그대로 붙여 준다.
    for l in lst:
        for e in l:
            answer.append(e[0])
    if answer[0] == "0": return "0"
    return "".join(answer)


print(solution(case8))
print(solution(case4))

# 87 878
# 878 87
