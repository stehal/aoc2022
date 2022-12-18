infile = "input.txt"

paths = [s.strip().replace(" -> ", " ").split(" ") for s in open(infile)]
paths2  = [[c.split(",")for c in p ] for p in paths ]
paths3 = [ list(zip(p, p[1:])) for p in [[ [int (xy) for xy in c] for c in p   ]    for p in paths2]]
moves = [(0, 1), (-1,1), (1,1)]

def coords(s, f):
    r = []
    for x in range(min([s[0],f[0]]),max([s[0],f[0]])+1):
        for y in range(min([s[1],f[1]]), max([s[1],f[1]])+1):
            r.append((x,y))
    return r

def init_cave(paths):
    cave = set()
    for p in paths:
        for segs in p:
            cave = cave | set(coords(segs[0], segs[1]))
    return cave

def init_max_depth(cave): 
    return max([c[1]for c in list(cave)])

def nexts(pos, moves):
    return [ tuple([sum(i) for i in zip(m,pos)]) for m in moves ]

def cant_move(cave, nexts, max_depth):
    if nexts[0][1] == max_depth + 2: return True
    return {n for n in nexts}.issubset(cave)

def drop(max_depth, moves, cave):
    pos = (500, 0)
    while True:
        if cant_move(cave, nexts(pos, moves), max_depth): 
            cave.add(pos)
            break
        else:
            pos = [n for n in nexts(pos, moves) if n not in cave][0]
        if pos[1] == max_depth:
            raise Exception("infinite drop")

def drop2(max_depth, moves, cave):
    pos = (500, 0)
    if pos in cave:
        raise Exception("done")
    
    while True:
        if cant_move(cave, nexts(pos, moves), max_depth): 
            cave.add(pos)
            break
        else:
            pos = [n for n in nexts(pos, moves) if n not in cave][0]

def solve(): 
    cave = init_cave(paths3)
    max_depth = init_max_depth(cave)
    count = 0
    try: 
        while True:
            drop(max_depth, moves, cave) 
            count +=1
    except Exception as e:
        print("Solution 1:", count)

def solve2(): 
    cave = init_cave(paths3)
    max_depth = init_max_depth(cave)
    count = 0
    try: 
        while True:
            drop2(max_depth, moves, cave) 
            count +=1
    except Exception as e:
        print("Solution 2:", count)

solve()
solve2()

