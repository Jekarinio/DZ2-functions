
# Дз1.
def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    return s

a, b = map(int, input().split())
print(sum_range(a, b))


# Дз2
import inspect


def inspect_function(f):
    print('Имя функции:', f.__qualname__)
    args = str(inspect.signature(foo))
    n = len(args)
    args = (args[1:n]).split(',')
    for arg in args:
        arg = arg.strip()
        p = arg.find('=')
        if p == -1:
            print("Позиционный ", arg)
        else:
            print("Ключевой    ", arg[0:p], "значение по умолчанию =", arg[p + 1:])


def foo(a, b, k=8):
    pass


# Дз3
import string

def is_pangram (gram):
    gram = gram.lower()
    gram_list_old = sorted([c for c in gram if c != ' '])
    gram_list = []
    for c in gram_list_old:
        if c not in gram_list:
            gram_list.append(c)
    if gram_list == list(string.ascii_lowercase): return True
    else: return False

# Дз4
from collections.abc import Hashable

def list_to_set(lst):
    st = {item for item in lst if isinstance(item, Hashable)}
    print(st)


# Дз5
def my_decorator(out=None):
    def decorator(func1):
        def a_wrapper(*arg1, **arg2):
            if arg1 in out:
                print("Уже запускалась функция с такими параметрами {}".format(arg1))
            else:
                out.append(arg1)
                answer = func1(*arg1, **arg2)
        return a_wrapper
    return decorator

@my_decorator()
def any_func(x, y):
    return x + y

for i in [(1,2), (2,3), (-1, 4), (1, 2)]:
    any_func(*i)
print(my_decorator.__defaults__)


# Дз6
def frange(start, end, step=0):
    i = start - step
    while i < end - step * 2:
        i += step
        yield round(i, len(str(step)) - 2)


for i in frange(1, 5):
    print(i)