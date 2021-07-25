def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_lst = list(skill)
        skill_set = set(skill)
        answer +=1
        for s in skill_tree:
            
            # 스킬트리선행조건이없다면 해당 스킬은 만족
            if len(skill_set) == 0:
                break 

            # 스킬트리 안에 해당 스킬이 있다면, if 제일 앞선 트리라면 그대로 진행/ else 선행트리가 있는 경우 멈추고 -1
            if s in skill_set:
                if skill_lst[0] == s:
                    skill_set.remove(s)
                    skill_lst.pop(0)
                    continue
                else: 
                    answer -=1
                    break
    return answer

a = "CBD"
b = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(a,b))


