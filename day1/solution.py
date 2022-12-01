infile = "input.txt"
#infile = "input_test.txt"
elves = []
elf = 0
for s in open(infile):
    
    try:
        elf += int(s.strip())
    except:
        elves.append(elf)
        elf=0

elves.append(elf)

print("Solution 1:")
print(max(elves))

elves.sort(reverse=True)

print("Solution 2:")
print(sum(elves[:3]))
    



    

