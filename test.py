def solution(k, room_number):
    answer = []
    check_lst = [i for i in range(k + 1)]
    for n in room_number:
        #  해당 방이 비어 있다면, 방을 주고 해당 칸을 다음 칸으로 패스
        if check_lst[n] == n:
            answer.append(n)
            check_lst[n] += 1
            temp = []
            #  다음 칸이 비어있지 않다면, 반복문 실행
            while check_lst[n] != n:
                temp.append(n)
                n = check_lst[n]  # 다음방이 안내하는 곳
            #  거쳤던 방에 빈방 값 저장
            for i in temp:
                check_lst[i] = n
        #  해당 방이 꽉 차 있다면
        else:
            #  빈 방을 찾는다.
            temp = []
            while check_lst[n] != n:
                temp.append(n)
                n = check_lst[n]
            #  빈 방을 찾고 나왔다면, 해당 칸을 주고 채워준다
            answer.append(n)
            check_lst[n] += 1
            #  다음 칸이 비어있지 않다면, 반복문 실행
            while check_lst[n] != n:
                temp.append(n)
                n = check_lst[n]
            #  거쳤던 방들에 빈방 값 저장
            for i in temp:
                check_lst[i] = n

    return answer


#print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(1,[1]))
