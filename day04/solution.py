infile = "input.txt"

assignments=[ s.strip().split(",") for s in open(infile)]

def two_sets(assignment):
    a1 = [int(n) for n in assignment[0].split("-")]
    a2 = [int(n) for n in assignment[1].split("-")]
    return set(range(a1[0], a1[1]+1)), set(range(a2[0], a2[1]+1))

def solution(assignments, l):
    return sum([l(*two_sets(a)) for a in assignments])
 

print(f'Solution 1: {solution(assignments, lambda r1, r2: r1.issubset(r2) or (r2).issubset(r1))}')

print(f'Solution 2: {solution(assignments, lambda r1, r2: len(set(r1) & set(r2)) > 0)}')
