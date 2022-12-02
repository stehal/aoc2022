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

print(f"Solution 1: {max(elves)}")

elves.sort(reverse=True)
print(f"Solution 2: {sum(elves[:3])}")
    



    

