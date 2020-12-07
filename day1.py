from functools import reduce
data = list(map(int, open('inputs/day1.txt', 'r').readlines()))

"""
def part1(ls):
    for i0, v0 in enumerate(ls):
        M0 = 2020 - v0
        ls_f0 = [v for i, v in enumerate(ls) if v <= M0 and i > i0]
        for v1 in ls_f0:
            if v0+v1 == 2020:
                print('value:', v0, v1)
                print('answer:', v0 * v1)


def part2(ls):
    for i0, v0 in enumerate(ls):
        M0 = 2020 - v0
        ls_f0 = [v for i, v in enumerate(ls) if v <= M0 and i > i0]
        for i1, v1 in enumerate(ls_f0):
            M1 = 2020 - (v0 + v1)
            ls_f1 = [v for i, v in enumerate(ls_f0) if v <= M1 and i > i1]
            for v2 in ls_f1:
                if v0+v1+v2 == 2020:
                    print('value:', v0, v1, v2)
                    print('answer:', v0 * v1 * v2)


part1(data)
part2(data)
"""


"""
def foreach(fn, iterable):
    for x in iterable:
        fn(x)


def prod(ls):
    return reduce(mul, ls, 1)


def check(ls):
    if sum(ls) == 2020:
        foreach(lambda v: print(v), ls)
        print(prod(ls))


def my_filter(M, idx, ls):
    return [v for i, v in enumerate(ls) if v <= M]


#foreach(lambda x: foreach(lambda y: check([x, y]), data), data)
#foreach(lambda x: foreach(lambda y: foreach(lambda z: check([x, y, z]), my_filter(x+y, data)), my_filter(x, data)), data)
"""


def prod(ls):
    return reduce(lambda a, b: a * b, ls, 1)


def answer(ls):
    return [sum(ls), prod(ls), ls]


part1 = [answer([x, y]) for ix, x in enumerate(data)
         for y in data[ix+1:] if sum([x, y]) == 2020]


part2 = [answer([x, y, z]) for ix, x in enumerate(data)
         for iy, y in enumerate(data[ix+1:]) if sum([x, y]) < 2020 for z in data[ix+1:][iy+1:] if sum([x, y, z]) == 2020]


print('[sum,', 'prod,', '[values]]')
print(part1)
print(part2)
