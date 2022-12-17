import functools
import numpy

infile = "input.txt"

def compare(p1,p2):
    """
    >>> compare([1,1,3,1,1],[1,1,5,1,1])
    -1
    >>> compare([[1],[2,3,4]], [[1],4])
    -1
    >>> compare([9], [[8,7,6]])
    1
    >>> compare([[4,4],4,4], [[4,4],4,4,4])
    -1
    >>> compare([7,7,7,7], [7,7,7])
    1
    >>> compare([], [3])
    -1
    >>> compare([[[]]], [[]])
    1
    >>> compare( [[]],[[[]]] )
    -1
    >>> compare([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9] )
    1
    >>> compare([[2]], [[2]])
    0
    """
    for p in zip(p1, p2):
        if type(p[0]) is int and type(p[1]) is int:
            if p[0] > p[1]: return 1
            if p[0] < p[1]: return -1
        elif type(p[0]) is list and type(p[1]) is int: 
            result = compare(p[0], [p[1]])
            if result !=  0: return result 
        elif type(p[0]) is int and type(p[1]) is list: 
            result = compare([p[0]], p[1])
            if result !=  0: return result
        elif type(p[0]) is list and type(p[1]) is list:  
            result = compare(p[0], p[1])
            if result != 0: return result 
    
    if len(p1) == len(p2): return 0
    if len(p1) < len(p2): return -1
    else: return 1

def solve1(grps):
    r = [compare(eval(grps[i]),eval(grps[i+1])) for i in range(0, len(grps)-3, 3)]
    return sum([i + 1 for i in range(0,len(r)) if r[i] == -1])

def solve2(grps):
    r= [eval(grps[i]) for i in range(0, len(grps)) if i%3 !=2]
    r.extend([[[2]],[[6]]])
    sorted_r = sorted(r, key=functools.cmp_to_key(compare))
    return numpy.prod([ i +1 for i in range(0,len(r)) if compare([[2]], sorted_r[i]) == 0 or compare([[6]], sorted_r[i]) == 0])

print("Solution 1", solve1([ s.strip() for s in open(infile)]))
   
print("Solution 2", solve2([ s.strip() for s in open(infile)]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
