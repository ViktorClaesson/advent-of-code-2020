data = open('inputs/day11.txt', 'r').read().splitlines()
data = [list(row) for row in data]


def game_of_life(ls, neighbors, threshold):
    copy = [list(sub_ls) for sub_ls in ls]

    # Game of life
    for y in range(len(ls)):
        for x in range(len(ls[y])):
            if ls[y][x] != '.':
                ns = neighbors(ls, x, y)
                if ls[y][x] == 'L' and ns == 0:
                    copy[y][x] = '#'
                elif ls[y][x] == '#' and ns >= threshold:
                    copy[y][x] = 'L'

    if all([x == y for x, y in zip(ls, copy)]):
        return ls
    else:
        return game_of_life(copy, neighbors, threshold)


def part1_check(ls, x, y):
    if y < 0 or y >= len(ls) or x < 0 or x >= len(ls[y]):
        return '.'
    else:
        return ls[y][x]


def part1_neighbors(ls, x, y):
    return sum([part1_check(ls, x + xo, y + yo) == '#' for yo in range(-1, 2) for xo in range(-1, 2) if not (yo == 0 and xo == 0)])


def part1(ls):
    return sum(sum(v == '#' for v in sub_ls) for sub_ls in game_of_life(ls, part1_neighbors, 4))


def part2_check(ls, x, y, xd, yd):
    if y < 0 or y >= len(ls) or x < 0 or x >= len(ls[y]):
        return '.'
    else:
        if ls[y][x] == '.':
            return part2_check(ls, x + xd, y + yd, xd, yd)
        else:
            return ls[y][x]


def part2_neighbors(ls, x, y):
    return sum([part2_check(ls, x + xd, y + yd, xd, yd) == '#' for yd in range(-1, 2) for xd in range(-1, 2) if not (yd == 0 and xd == 0)])


def part2(ls):
    return sum(sum(v == '#' for v in sub_ls) for sub_ls in game_of_life(ls, part2_neighbors, 5))


print('Answer part 1:', part1(data))
print('Answer part 2:', part2(data))
