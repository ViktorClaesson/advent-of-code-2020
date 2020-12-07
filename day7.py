def convert_to_bag(line):
    outer, inner = line.replace('no other', '').replace(' bags', '').replace(
        ' bag', '').replace('.', '').split(' contain ')
    return outer, [ls.split(' ', 1) for ls in inner.split(', ') if len(inner) > 0]


def bag_contains_shiny_gold(bag, bags):
    if not bags[bag]:
        return False

    return 'shiny gold' in [b for a, b in bags[bag]] or any(bag_contains_shiny_gold(b, bags) for a, b in bags[bag])


def bags_in_bag(bag, bags):
    if not bags[bag]:
        return 0

    return sum([int(a) + int(a) * bags_in_bag(b, bags) for a, b in bags[bag]])


data = open('inputs/day7.txt', 'r').read().splitlines()
bags = dict(map(convert_to_bag, data))

print('Answer part 1:', len(
    [1 for bag in bags.keys() if bag_contains_shiny_gold(bag, bags)]))
print('Answer part 2:', bags_in_bag('shiny gold', bags))
