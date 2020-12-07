data = open('inputs/day2.txt', 'r').read().splitlines()


def check1(line):
    size, char, password = line.split(' ')
    mn, mx = map(int, size.split('-'))
    char = char.replace(':', '')
    amnt = len(filter(lambda c: c == char, password))
    return (amnt >= mn and amnt <= mx)


def check2(line):
    size, char, password = line.split(' ')
    mn, mx = map(int, size.split('-'))
    char = char.replace(':', '')
    b1 = (password[mn - 1] == char and password[mx - 1] != char)
    b2 = (password[mn - 1] != char and password[mx - 1] == char)
    return b1 or b2


print(len(filter(check1, data)))
print(len(filter(check2, data)))
