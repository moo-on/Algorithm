#
#
#
#
#
#
#
#
#
#
#
#
from collections import deque


def solution(n, k, cmd):
    answer = ''
    read_only = [i for i in range(n)]
    undo = deque([])
    log = []

    for command in cmd:
        c = command.split()

        if c[0] == "U":
            c[1] = int(c[1])
            k -= c[1]

        if c[0] == "D":
            c[1] = int(c[1])
            k += c[1]

        if c[0] == "C":
            undo.append(read_only.pop(k))
            log.append(k)

            if len(read_only) - 1 == k:  # last section
                k -= 1
                log[-1] = "end"

        if c[0] == "Z":
            u = undo.pop()
            l = log.pop()

            if u < read_only[k]:
                k += 1
            if l == "end":
                read_only.append(u)
                continue
            read_only.insert(l, u)

        answer = ["X" for _ in range(n)]
        for e in read_only:
            answer[e] = "O"

    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
