#[1, 1, 9, 1, 1, 1]	0	5



def solution(priorities, location):
    answer = []
    MAX = max(priorities)
    lst = [i for i in range(len(priorities))]
    lst_answer = []

    while priorities:
        if MAX == priorities[0]:
            answer.append(priorities[0])
            del priorities[0]

            lst_answer.append(lst[0])
            del lst[0]

            if not priorities: break
            MAX = max(priorities)
        else:
            priorities.append(priorities[0])
            del priorities[0]

            lst.append(lst[0])
            del lst[0]

    print(answer)
    print(lst_answer.index(location) + 1)
    return answer

if __name__ =="__main__":
    solution([1, 1, 9, 1, 1, 1], 0)
    solution([2, 1, 3, 2],2)