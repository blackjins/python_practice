def do_twice(func, arg):
    x = func(arg)
    return func(x)

def three_times(num):
    return num * 3

do_twice(three_times, 2)
three_times(three_times(2))
