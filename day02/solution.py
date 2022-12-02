infile = "input.txt"
#infile = "input_test.txt"

score = {"A X":4,"A Y":8,"A Z":3,"B X":1,"B Y":5,"B Z":9,"C X":7,"C Y":2,"C Z":6}
score2 = {"A X":3,"A Y":4,"A Z":8,"B X":1,"B Y":5,"B Z":9,"C X":2,"C Y":6,"C Z":7}

print(f"Solution 1: {sum([score.get(s.strip()) for s in open(infile)])}")
print(f"Solution 2: {sum([score2.get(s.strip()) for s in open(infile)])}")