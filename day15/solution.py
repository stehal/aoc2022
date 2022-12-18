def manhattan(c1, c2):
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])

def excluded_in_row(row, sensor, beacon):
    dist = manhattan(sensor, beacon)
    q = dist
    if not (sensor[1]-dist) <= row <= (sensor[1]+dist): 
        return None 
    if row > sensor[1]: q=dist-row+sensor[1]
    if row < sensor[1]: q=dist-sensor[1] +row
    return sorted([sensor[0]-q, sensor[0]+q])

def all_exluded_in_row(row, s_and_b):
    return sorted([a for a in [excluded_in_row(row, sb[0], sb[1]) for sb in s_and_b] if a is not None])

def solve(row, s_and_b):
    aeir =  all_exluded_in_row(row, s_and_b)
    count = aeir[0][1] - aeir[0][0]
    previous = aeir[0]
    for r in aeir[1:]:
        if r[0] <= previous[1] and r[1] >= previous[1]:
            count += r[1] - previous[1]
            previous = r
        if r[0] > previous[1]:
            count += r[1] - r[0]
            previous = r
    return count

def solve2(maxr, s_and_b):
    for row in range(maxr+1):
        aeir = all_exluded_in_row(row, s_and_b)
        previous = aeir[0]
        for r in aeir[1:]:
            if r[1] >=0:
                if r[0] <= previous[1] +1 and r[1] >= previous[1]:
                    previous = r
                if r[0] > previous[1] +1:
                    return (r[0] -1) * 4000000 + row
            if r[1]> maxr:break

infile = "input.txt"
a1 = [s.strip().replace(",", "").replace(":", "").replace("=", " ").split(" ") for s in open(infile)]
s_and_b = [ [(int(s[3]), int(s[5])),(int(s[11]), int(s[13]))] for s in a1] 

print("Solution 1:",solve(2000000, s_and_b))
print("Solution 2:",solve2(4000000, s_and_b))