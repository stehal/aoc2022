from collections import defaultdict

infile = "input.txt"
width = 9
initial_height = 8
lines = [l for l in open(infile)]

def parse_move(move):
    m = move.split(" ")
    return [int(m[1]),int(m[3]),int(m[5])]

def parse_moves(move):
    return  [parse_move(l) for l in lines[initial_height + 2:]]

moves = parse_moves(lines)

def split_line(line, width):
    return [line[i] for i in range(1,4 * width,4)]

def parse_stack(infile):
    stacklines = reversed([split_line(l,width) for l in lines[:initial_height]])
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
    top = []
    for n in range(0, m[0]):
        top.append(stack[m[1]].pop())
    stack[m[2]].extend(reversed(top))

def solution(func):
    stack = parse_stack(infile)
    for m in moves:
        func(m, stack)
    return "".join( [stack[i].pop() for i in range(1, width + 1)])
    
print(f'Solution 1: {solution(do_move)}')
print(f'Solution 2: {solution(do_move2)}')