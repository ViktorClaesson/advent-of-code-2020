import math

data = open('inputs/day3.txt', 'r').read().splitlines()


def check(position):
    row = data[position[1]]
    width = len(row)
    return row[position[0] % width] == '#'


def trees(vel):
    goal = len(data)
    iterations = int(goal / vel[1])
    return len([i for i in range(iterations) if check((vel[0] * i, vel[1] * i))])


p1 = trees((1, 1))
p2 = trees((3, 1))
p3 = trees((5, 1))
p4 = trees((7, 1))
p5 = trees((1, 2))

print('Answer part 1:', p2)
print('Answer part 2:', p1*p2*p3*p4*p5)
