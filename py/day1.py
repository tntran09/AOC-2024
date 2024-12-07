import fileinput
import re

def run():
    lines = []
    one = []
    two = []
    for line in fileinput.input(files="input/test_1.txt"):
        lines.append(line)
    for line in lines:
        parts = re.split('\\s+', line)
        one.append(int(parts[0]))
        two.append(int(parts[1]))
    one.sort()
    two.sort()

    sum = 0
    for i in range(len(one)):
        sum += abs(one[i] - two[i])

    print(sum)

def part2():
    one = []
    two = []
    counts = dict()

    for line in fileinput.input(files="input/test_1.txt"):
        parts = re.split('\\s+', line)
        one.append(int(parts[0]))
        two.append(int(parts[1]))
    
    n = len(one)
    sum = 0
    for i in range(n):
        counts[i] = two.count(one[i]) if i not in counts else counts[i]
        sum += one[i] * counts[i]

    print(sum)
