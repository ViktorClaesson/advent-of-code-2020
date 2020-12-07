data = open('inputs/day5.txt', 'r').read().splitlines()


def pick(char, min, max):
    mid = int((min + max) / 2)
    if char == 'F' or char == 'L':
        return min, mid
    elif char == 'B' or char == 'R':
        return mid+1, max


def bin_2_num(bin):
    min = 0
    max = 2**len(bin)-1
    for char in bin:
        min, max = pick(char, min, max)
    return min


def seat(bin):
    row = bin_2_num(bin[:7])
    col = bin_2_num(bin[7:])
    return row * 8 + col


seats = sorted(map(seat, data))
for idx, curr in enumerate(seats):
    prev = seats[idx - 1]
    next = seats[(idx + 1) % len(seats)]
    if curr != prev + 1 or curr != next - 1:
        print(idx, curr)
