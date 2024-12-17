import fileinput
from functools import reduce
import re

def part1():
    reports = []

    for line in fileinput.input(files="input/test_2.txt"):
        reports.append([int(x) for x in re.split('\\s+', (line)) if len(x) > 0])

    sum = 0
    
    for row in reports:
        increasing = True
        decreasing = True
        for i in range(len(row) - 1):
            if row[i] <= row[i + 1] or row[i] - row[i + 1] > 3: decreasing = False
            if row[i] >= row[i + 1] or row[i + 1] - row[i] > 3: increasing = False
        
        sum += 1 if (increasing and not decreasing) or (not increasing and decreasing) else 0
    
    print(sum)

def part2():
    reports = []

    for line in fileinput.input(files="input/test_2.txt"):
        reports.append([int(x) for x in re.split('\\s+', (line)) if len(x) > 0])

    sum = 0
    
    for row in reports:
        for j in range(len(row)):
            splicedRow = row[0:j] + row[j+1:]
            increasing = True
            decreasing = True
            for i in range(len(splicedRow) - 1):
                if splicedRow[i] <= splicedRow[i + 1] or splicedRow[i] - splicedRow[i + 1] > 3: decreasing = False
                if splicedRow[i] >= splicedRow[i + 1] or splicedRow[i + 1] - splicedRow[i] > 3: increasing = False
        
            if (increasing and not decreasing) or (not increasing and decreasing):
                sum += 1
                break
    
    print(sum)