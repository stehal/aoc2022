infile = "input.txt"

trees = [[int(x) for x in s.strip()] for s in open(infile)]

height = len(trees)

seen = set()

def from_top(trees):
    for col in range(0,height):
        p = -1
        for row in range(0, height):
            th = trees[row][col]
            if th > p:
                seen.add((row,col))
                p=th

def from_bottom(trees):
    for col in range(0, height):
        p = -1
        for row in range(height-1, -1, -1):
            th = trees[row][col]
            if th > p:
                seen.add((row,col))
                p=th

def from_left(trees):
    for row in range(0, height):
        p = -1
        for col in range(0, height):
            th = trees[row][col]
            if th > p:
                seen.add((row,col))
                p=th

def from_right(trees):
    for row in range(0, height):
        p = -1
        for col in range(height-1,-1,-1):
            th = trees[row][col]
            if th > p:
                seen.add((row,col))
                p=th

def from_tree(row,col):
    a=[]  
    for c in range(col + 1, height):
        a.append(1)
        if trees[row][c] >= trees[row][col]: break
        
    b = []
    for c in range(col-1, -1, -1):
        b.append(1)
        if trees[row][c] >= trees[row][col]: break
       
    c=[]
    for r in range(row+1, height):
        c.append(1)
        if trees[r][col] >= trees[row][col]: break
       
    d=[]
    for r in range(row-1, -1, -1):
        d.append(1)
        if trees[r][col] >= trees[row][col]: break
   
    return sum(a)*sum(b)*sum(c)*sum(d)
            
from_top(trees)
from_bottom(trees)
from_left(trees)
from_right(trees)
print(f'Solution 1: {len(seen)}')
print(f'Solution 2: {max([from_tree(r,c) for c in range(1,height -1) for r in range(1,height-1)])}')

