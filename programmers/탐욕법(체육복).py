import copy

def solution(n, lost, reserve):
    rich = list(set(reserve) - set(lost))
    poor = list(set(lost) - set(reserve))
    poor_copy = copy.deepcopy(poor)

    for e in poor_copy:
        if e-1 in rich:
            poor.remove(e)
            rich.remove(e-1)
        elif e+1 in rich:
            poor.remove(e)
            rich.remove(e+1)

    return n-len(poor)


print(solution(5,[2,4], [1,3,5]))



