infile = "input.txt"

def listzip(text, size):
    return list(zip(*[text[i:] for i in range(0,size)]))

def solution(packets):
    packetlength = len(packets[0])
    for i in range(0, len(packets)):
        if len(set(packets[i])) == packetlength: return i + packetlength

print(f'Solution 1: {solution(listzip(open(infile).read(),4))}')
print(f'Solution 2: {solution(listzip(open(infile).read(),14))}')
