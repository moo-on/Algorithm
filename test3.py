di, dj = [1, -1, 0, 0], [0, 0, 1, -1]  # down, up, right, left
sub_d = [1, -1]
len_ = 5


def check(i, j, place):
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < len_ and 0 <= nj < len_:
            if place[ni][nj] == "P": return False
            if place[ni][nj] == "O":
                for d in sub_d:
                    if di[n] == 0:
                        ni = i + di[n] + d
                        nj = j + dj[n]
                    elif dj[n] == 0:
                        ni = i + di[n]
                        nj = j + dj[n] + d
                    if 0 <= ni < len_ and 0 <= nj < len_:
                        if place[ni][nj] == "P": return False
    return True


def solution(places):
    answer = []
    # explore the room
    for place in places:

        # casting room form
        temp_place = []
        temp_answer = []
        for p in place:
            temp_place.append(list(p))

        for i in range(len(place)):
            for j in range(len(place)):
                if place[i][j] == "P":
                    if not check(i, j, temp_place):
                        temp_answer.append(0)
                        break
            if 0 in temp_answer:
                break

        if 0 in temp_answer:
            answer.append(0)
        else:
            answer.append(1)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
