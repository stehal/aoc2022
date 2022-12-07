from anytree import Node, RenderTree, Walker

infile = "input.txt"

root = Node(".", type="dir")
current = root

for s in open(infile):
    line = s.strip().split(" ")
    f = line[0]
    if f.startswith("dir"):
        Node(line[1], parent=current, type="dir")
    elif f.startswith("$"):
        if line[1] == 'cd':
            if line[2] == "..":
                current = current.parent
            else:
                for c in current.children:
                    if line[2] == c.name:
                        current = c
                        break
    else:
        child = Node(line[1], parent=current, type="file", size=int(f))

alldirs = []

def sumdir(dir):
    dirsum = 0
    for child in dir.children:
        if child.type == "file":
            dirsum += child.size
        else:
            dirsum += sumdir(child)
    alldirs.append(dirsum)
    return dirsum
 
sumdir(root)
alldirs.sort()

print(f'Solution 1: {sum([d for d in alldirs if d < 100000])}')
print(f'Solution 2: {[d for d in alldirs if d > alldirs[-1] - 40000000][0]}')
