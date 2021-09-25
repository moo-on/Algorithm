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

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))

solution(case1)