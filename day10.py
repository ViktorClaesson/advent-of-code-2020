data = open('inputs/day10.txt', 'r').read().splitlines()
data = [int(x) for x in data]
device = max(data) + 3
data = sorted([0, device] + data)


def part1(ls):
    diffs = [pair[1] - pair[0] for pair in zip(ls[:-1], ls[1:])]
    ones = len([x for x in diffs if x == 1])
    threes = len([x for x in diffs if x == 3])
    return ones * threes


def part2(ls):
    memory = [0] * len(ls)
    return part2_rec(ls, memory, 0)


def part2_rec(ls, memory, idx):
    if memory[idx] != 0:
        return memory[idx]

    curr = ls[idx]
    valid = [i for i, v in enumerate(ls) if v > curr and v <= curr + 3]
    if not valid:
        return 1

    ret = sum([part2_rec(ls, memory, i) for i in valid])
    memory[idx] = ret
    return ret


print('Answer part 1:', part1(data))
print('Answer part 2:', part2(data))
