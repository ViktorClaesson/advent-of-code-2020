def is_loop(instructs):
    ins = 0
    acc = 0
    memory = [False] * len(instructs)
    while ins < len(instructs) and not memory[ins]:
        memory[ins] = True
        if instructs[ins][0] == 'acc':
            acc += instructs[ins][1]
        elif instructs[ins][0] == 'jmp':
            ins += instructs[ins][1] - 1
        ins += 1

    return (ins < len(instructs), acc)


def invert(ins):
    if ins[0] == 'nop':
        return ['jmp', ins[1]]
    elif ins[0] == 'jmp':
        return ['nop', ins[1]]
    else:
        return ins


def alter(instructs, i):
    ret = list(instructs)
    ret[i] = invert(ret[i])
    return ret


with open('inputs/day8.txt', 'r') as file:
    instructs = file.read().splitlines()
    instructs = [line.split(' ') for line in instructs]
    instructs = [(a, int(b)) for a, b in instructs]

    print('Answer part 1:', is_loop(instructs))
    print('Answer part 2:', next((loop, val) for loop, val in [is_loop(alter(instructs, i))
                                                               for i in range(len(instructs))] if not loop))
