data = open('inputs/day6.txt', 'r').read().splitlines()
data = ','.join(data)
data = data.split(',,')

data1 = map(lambda line: line.replace(',', ''), data)
data1 = map(lambda line: len(set(line)), data1)
ans1 = sum(data1)


def calc(line):
    ans_ls = line.split(',')
    qs = set(line.replace(',', ''))
    return len([q for q in qs if all([q in ans for ans in ans_ls])])


data2 = map(calc, data)
ans2 = sum(data2)


print('Answer part 1:', ans1)
print('Answer part 1:', ans2)
