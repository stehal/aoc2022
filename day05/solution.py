from collections import defaultdict

infile = "input.txt"
width = 9
initial_height = 8
lines = [l for l in open(infile)]

def parse_move(move):
    m = move.split(" ")
    return [int(m[1]),int(m[3]),int(m[5])]

def parse_stack(infile):
    stacklines = reversed([[line[i] for i in range(1,4 * width,4)] for line in lines[:initial_height]])
    stack = defaultdict(list)
    for line in stacklines:
        for col in range(1, width +1):
            a = line[col -1]
            if a != " ": stack[col].append(line[col -1])
    return stack

def do_move(m,stack):
    for n in range(0,m[0]):
        top = stack[m[1]].pop()
        stack[m[2]].append(top)

def do_move2(m, stack):
    top = [stack[m[1]].pop() for n in range(0, m[0])]
    stack[m[2]].extend(reversed(top))

def solution(func):
    moves = [parse_move(l) for l in lines[initial_height + 2:]]
    stack = parse_stack(infile)
    for m in moves:
        func(m, stack)
    return "".join( [stack[i].pop() for i in range(1, width + 1)])
    
print(f'Solution 1: {solution(do_move)}')
print(f'Solution 2: {solution(do_move2)}')