import string

infile = "input.txt"
#infile = "input_test.txt"

def sum_priorities(items):
    x = sum([string.ascii_lowercase.index(c)+1 for c in items if c.islower()]) 
    y = sum([string.ascii_uppercase.index(c)+27 for c in items if c.isupper()])
    return x+y

rucsacks = [s.strip() for s in open(infile)]
commonitems = [next(iter(set(s[:int(len(s)/2)]).intersection( set(s[int(len(s)/2):])))) for s in rucsacks]

print(f'Solution 1: {sum_priorities(commonitems)}')

groups = [[rucsacks[i], rucsacks[i+1], rucsacks[i+2]] for i in range(0, len(rucsacks), 3)]
commonitems2 = [next(iter(set(h[0])& set(h[1])&set(h[2])))for h in groups]

print(f'Solution 2: {sum_priorities(commonitems2)}')



