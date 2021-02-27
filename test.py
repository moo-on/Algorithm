import sys

input = sys.stdin.readline


def main():
    skill_lst = input().split()
    n = int(input())
    as_lst = [input().split() for _ in range(n)]



    print(as_lst)


if __name__ == "__main__":
    main()