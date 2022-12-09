infile = "input.txt"

moves = [(s.strip().split()[0], int(s.strip().split()[1])) for s in open(infile)]
map_dir = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

def head_move(pos, direction):
    return tuple(map(sum, zip(pos, map_dir[direction])))

def diff(t):
    return t[1] - t[0]

def move_following(knot, following_knot):
    d = tuple(map(diff, zip(knot, following_knot)))
    dx,dy = 0,0
    if abs(d[0]) == 2:
        dx = -int(2/d[0])
        if abs(d[1]) > 0: dy = int(abs(d[1])/-d[1])
    elif abs(d[1]) == 2: 
        dy = -int(2/d[1])
        if abs(d[0]) > 0: dx = int(abs(d[0])/-d[0])
    return tuple(map(sum, zip(following_knot, (dx,dy))))
        
def do_move(knots, direction):
    knots[0] = tuple(map(sum, zip(knots[0], map_dir[direction])))
    for i in range(1,len(knots)):
        knots[i] = move_following(knots[i-1], knots[i])  
    return knots

def solve(no_of_knots):
    knots =[(0,0)]*no_of_knots
    tail_positions = set()
    tail_positions.add(knots[no_of_knots-1])
    for m in moves:
        direction = m[0]
        for i in range(0, m[1]):
            knots = do_move(knots, direction)
            tail_positions.add(knots[no_of_knots-1])
    return len(tail_positions)

print(f'Solution 1: {solve(2)}')
print(f'Solution 2: {solve(10)}')
