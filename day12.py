data = open('inputs/day12.txt', 'r').read().splitlines()
data = [(row[0], int(row[1:])) for row in data]


def part1(ls):
    N = sum(ins[1] for ins in ls if ins[0] == 'N')
    S = sum(ins[1] for ins in ls if ins[0] == 'S')
    E = sum(ins[1] for ins in ls if ins[0] == 'E')
    W = sum(ins[1] for ins in ls if ins[0] == 'W')

    x = E - W
    y = N - S
    rot = 0
    for ins, val in [(ins, val) for ins, val in ls if (ins == 'F' or ins == 'R' or ins == 'L')]:
        if ins == 'F':
            if rot == 0:
                x += val
            elif rot == 90:
                y -= val
            elif rot == 180:
                x -= val
            elif rot == 270:
                y += val
        elif ins == 'R':
            rot = (rot + val) % 360
        elif ins == 'L':
            rot = (360 + rot - val) % 360

    return abs(x) + abs(y)


def part2(ls):
    pos = (0, 0)
    waypoint = (10, 1)
    for ins, val in ls:
        if ins == 'N':
            waypoint = (waypoint[0], waypoint[1] + val)
        elif ins == 'S':
            waypoint = (waypoint[0], waypoint[1] - val)
        elif ins == 'E':
            waypoint = (waypoint[0] + val, waypoint[1])
        elif ins == 'W':
            waypoint = (waypoint[0] - val, waypoint[1])
        elif ins == 'L':
            for i in range(int(val / 90)):
                waypoint = (-waypoint[1], waypoint[0])
        elif ins == 'R':
            for i in range(int(val / 90)):
                waypoint = (waypoint[1], -waypoint[0])
        elif ins == 'F':
            pos = (pos[0] + val * waypoint[0], pos[1] + val * waypoint[1])
    return abs(pos[0]) + abs(pos[1])


print('Answer part 1:', part1(data))
print('Answer part 2:', part2(data))
