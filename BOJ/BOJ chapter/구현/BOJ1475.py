from collections import Counter,defaultdict
import math
lst = map(int, list(str(input())))

dic = dict(Counter(lst))
if 6 not in dic: dic[6] = 0
if 9 not in dic: dic[9] = 0
dic[6], dic[9] = math.ceil((dic[6]+dic[9])/2), 0

print(max(dic.values()))