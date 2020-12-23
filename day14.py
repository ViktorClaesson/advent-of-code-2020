def bitify(s):
    return f'{int(s):036b}'


def val_parse(val, mask):
    return sum(int(bit) * 2**(35-idx) for idx, bit in enumerate([m if m != 'X' else v for v, m in zip(bitify(val), mask)]))


def part1(row, mem, mask):
    mem[row[1]] = val_parse(row[2], mask)


def split_addr(addr, idx):
    left = list(addr)
    left[idx] = '0'
    right = list(addr)
    right[idx] = '1'
    return left, right


def addr_parse(addr):
    idx = 0
    addrs = [list(addr)]
    while idx < len(addr):
        if addr[idx] == 'X':
            addrs = [item for ls in [split_addr(
                addr, idx) for addr in addrs] for item in ls]
        idx += 1

    return [''.join(addr) for addr in addrs]


def part2(row, mem, mask):
    magic_addr = [m if m != '0' else a for a, m in zip(bitify(row[1]), mask)]
    addrs = addr_parse(magic_addr)
    for addr in addrs:
        mem[addr] = int(row[2])


def main(ls, func):
    mask = ''
    mem = {}
    for row in ls:
        if row[0] == 'mask':
            mask = row[1]
        elif row[0] == 'mem':
            func(row, mem, mask)

    return sum(mem.values())


data = open('inputs/day14.txt', 'r').read().splitlines()
data = [row.split(' = ') for row in data]
data = [[*row[0].replace(']', '').split('['), row[1]] for row in data]


print('Answer part 1:', main(data, part1))
print('Answer part 2:', main(data, part2))
