#[1, 1, 9, 1, 1, 1]	0	5



def solution(priorities, location):
    answer = 0
    location_id = id(priorities[location])


    return answer

lst = [1,2,3]
print(id(lst[1]))
lst2 = []
lst2.append(lst[1])
print(id(lst2[0]))

lst.append(lst[1])

print(id(lst[-1]))
lst.append(2)
print(id(lst[-1]))