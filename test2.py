import sys
from collections import Counter

input = sys.stdin.readline


def main():
    input_lst = list(input().rstrip())

    cnt = Counter(input_lst)
    print(cnt)
    if cnt['('] > cnt[')']:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()