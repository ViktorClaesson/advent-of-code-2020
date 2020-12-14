data = open('inputs/day13.txt', 'r').read().splitlines()


def part1(ls):
    reference = int(data[0])
    busses = [int(buss) for buss in data[1].split(',') if buss != 'x']
    buss_wait = [(buss, (buss - (reference % buss)) % buss) for buss in busses]
    min_wait = min(buss_wait, key=lambda t: t[1])
    return min_wait[0] * min_wait[1]


def part2(ls):
    busses = [(int(buss), idx)
              for idx, buss in enumerate(data[1].split(',')) if buss != 'x']
    for buss, idx in busses:
        print(buss, idx, idx % buss)
    return 0


print('Answer part 1:', part1(data))
print('Answer part 2:', part2(data))
