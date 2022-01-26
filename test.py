from collections import deque


def solution(n, k, cmd):
    answer = ''
    link_dict = {}
    for i in range(n):
        link_dict[i] = {"prev": i - 1, "next": i + 1}
    link_dict[0]["prev"], link_dict[n - 1]["next"] = "head", "tail"
    link_dict["head"] = {next: 0}

    print(link_dict)

    undo = []
    for command in cmd:
        c = command.split()

        if c[0] == "U":
            for _ in range(int(c[1])):
                k = link_dict[k]["prev"]

        if c[0] == "D":
            for _ in range(int(c[1])):
                k = link_dict[k]["next"]

        if c[0] == "C":
            prev, next = link_dict[k]["prev"], link_dict[k]["next"]
            undo.append(k)

            if prev == "head":
                link_dict[prev]["next"] = link_dict[k]["next"]
                link_dict[next]["prev"] = link_dict[k]["prev"]
                k = link_dict[k]["next"]
                continue

            if next == "tail":
                link_dict[prev]["next"] = link_dict[k]["next"]
                k = link_dict[k]["prev"]
                continue

            link_dict[prev]["next"] = link_dict[k]["next"]
            link_dict[next]["prev"] = link_dict[k]["prev"]
            k = link_dict[k]["next"]

        if c[0] == "Z":
            node = undo.pop()
            prev, next = link_dict[node]["prev"], link_dict[node]["next"]

            if prev == "head":
                link_dict[next]["prev"] = node
                continue

            if next == "tail":
                link_dict[prev]["next"] = node
                continue

            link_dict[prev]["next"] = node
            link_dict[next]["prev"] = node

    return link_dict


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
