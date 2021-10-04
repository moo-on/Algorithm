import sys
input = sys.stdin.readline

n = int(input())
input_lst = list(map(int, input().split()))
find_n = int(input())

def binary_s(lst, answer, start, end):
    mid = (start + end)//2
    if start < end: return None
    if lst[mid] == answer: return mid
    elif lst[mid] < answer: return binary_s(lst, answer, mid+1, end)
    elif lst[mid] > answer: return binary_s(lst, answer, start, mid-1)

print(binary_s(input_lst, find_n, 0, n-1))
