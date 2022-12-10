infile = "input.txt"

instructions =[s.strip().split(" ") for s in open(infile)]

def x_register(instructions):
    x=[]
    for i in instructions:
        if i[0] == "addx": 
            x.append(0)
            x.append(int(i[1]))
        else:
            x.append(0)
    return [sum(x[:n]) +1 for n in range(0, len(x))]
    
def solve(instructions):
    x = x_register(instructions)
    return sum([x[n]*(n+1) for n in range(19, len(x),40)])

def solve2(instructions):
    crt = ["\n"]
    x = x_register(instructions)
    for cycle in range(1, len(x) +1):
        sprite_pos = x[cycle-1]%40 
        if sprite_pos-1 <= (cycle-1)%40 <= sprite_pos+1:
            crt.append("#")
        else: crt.append(".")
        if cycle%40 == 0:
            crt.append("\n")
    return ''.join(crt)


print(f'Solution 1: {solve(instructions)}')
print(f'Solution 2: {solve2(instructions)}')
