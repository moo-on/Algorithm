
def test():
    parameter.append(4)

def func(lst):
    global parameter
    parameter = []

    test()
    print(parameter)
    return

func([1,2,3])




#  결과: [4]