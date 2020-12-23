import functools
import itertools

data = open('inputs/day13.txt', 'r').read().splitlines()


def part1(ls):
    reference = int(data[0])
    busses = [int(buss) for buss in data[1].split(',') if buss != 'x']
    buss_wait = [(buss, (buss - (reference % buss)) % buss) for buss in busses]
    min_wait = min(buss_wait, key=lambda t: t[1])
    return min_wait[0] * min_wait[1]


def prod(ls):
    return functools.reduce(lambda a, c: a * c, ls, 1)


def index_to_term(busses, idx):
    buss_i = busses[idx][0]
    goal_i = busses[idx][1]
    factors_i = [buss for buss, _ in busses if buss != buss_i]
    term_i = prod(factors_i)
    small_term_i = term_i % buss_i
    k = next(i for i in itertools.count(1, 1) if (
        small_term_i * i) % buss_i == goal_i)
    kn = next(i for i in itertools.count(-1, -1) if (
        small_term_i * i) % buss_i == goal_i)
    return term_i * k, term_i * kn


def all_sums(ls, idx):
    if idx >= len(ls):
        return [0]

    sub_ls = all_sums(ls, idx + 1)
    left = [x + ls[idx][0] for x in sub_ls]
    right = [x + ls[idx][1] for x in sub_ls]
    return left + right


def part2(ls):
    busses = enumerate(data[1].split(','))
    busses = [(int(buss), idx) for idx, buss in busses if buss != 'x']
    busses = [(buss, (buss - (idx % buss)) % buss) for buss, idx in busses]

    term_c = len(busses) - 1
    terms = [index_to_term(busses, i+1) for i in range(term_c)]

    least_sum = sorted([x for x in all_sums(terms, 0) if x > 0])[0]
    return least_sum


print('Answer part 1:', part1(data))
print('Answer part 2:', part2(data))
