import copy


def solution(n):
    prefixes = ['1', '2', '4']
    records = ['1', '2', '4']

    if n <= 3:
        return records[n - 1]
    cnt = 3

    while True:
        temp_records = copy.deepcopy(records)
        records = []
        for prefix in prefixes:
            for record in temp_records:
                records.append(''.join([prefix, record]))
                cnt += 1
                if cnt == n:
                    return records[-1]


print(solution(16))

# 1 1
# 2 2
# 3 4
#
# 4 11
# 5 12
# 6 14
# 7 21
# 8 22
# 9 24
# 10 41
# 11 42
# 12 44
#
# 13 111
# 14 112
# 15 114
# 16 121
# 17 122
