import sys
input = sys.stdin.readline

n = int(input())
s = set()

def add(s, e):
    s.add(e)

def remove(s, e):
    s.discard(e)

def check(s, e):
    if e in s:
        print(1)
    else:
        print(0)

def toggle(s, e):
    if e in s: s.discard(e)
    else: s.add(e)

def all():
    global s
    s = {str(i) for i in range(1, 21)}

def empty():
    s.clear()

functions = {'add': add,
             'remove' :remove,
             'check' : check,
             'toggle' : toggle,
             'all' : all,
             "empty" : empty}


for _ in range(n):
    l = input().rstrip().split()
    func = functions[l[0]]

    if len(l) == 1:
        func()

    else:
        func(s, l[1])