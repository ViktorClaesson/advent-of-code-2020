data = open('inputs/day9.txt', 'r').read().splitlines()
data = [int(x) for x in data]


def check(ls, idx):
    lo = max(0, idx - 25)
    hi = min(len(ls), idx)
    pre = ls[lo:hi]
    return any(x == ls[idx] for x in [pre[i] + pre[j] for i in range(25) for j in range(25) if i < j])


def part1(ls):
    return next(ls[i] for i in range(25, len(ls)) if not check(ls, i))


def part2(ls, p1):
    return next(min(ls[i:j]) + max(ls[i:j]) for i in range(len(ls))
                for j in range(len(ls)) if i+1 < j if sum(ls[i:j]) == p1)


p1 = part1(data)
print('Answer part 1:', p1)
print('Answer part 2:', part2(data, p1))
