import fileinput
import re
import pdb

def part1():
    # pdb.set_trace()
    rules = {}
    readRules = True
    sum = 0
    for line in fileinput.input(files="input/test_5.txt"):
        if re.match(r'\s+', line):
            readRules = False
            print(rules)
            continue
        if readRules:
            rule = [int(x) for x in re.split(r'[\s\|]+', (line)) if len(x) > 0]
            key = rule[0]
            rules[key] = rules[key] if key in rules else []
            rules[key].append(rule[1])
        else:
            pages = [int(x.strip()) for x in line.split(',')]
            valid = True
            for x in range(0, len(pages) - 1):
                for y in range(x + 1, len(pages)):
                    if pages[x] in rules:
                        if pages[y] in rules[pages[x]]:
                            continue
                    if pages[y] in rules:
                        if pages[x] in rules[pages[y]]:
                            valid = False
                            break
                if not valid:
                    break
            
            if valid:
                mid = int(pages[int(len(pages) / 2)])
                # print(f'adding {mid}')
                sum += mid
    print(sum)

def part2():
    rules = {}
    readRules = True
    sum = 0
    for line in fileinput.input(files="input/test_5.txt"):
        if re.match(r'\s+', line):
            readRules = False
            print(rules)
            continue

        if readRules:
            rule = [int(x) for x in re.split(r'[\s\|]+', (line)) if len(x) > 0]
            key = rule[0]
            rules[key] = rules[key] if key in rules else []
            rules[key].append(rule[1])
        else:
            pages = [int(x.strip()) for x in line.split(',')]
            swapped = False
            x = 0
            while x < len(pages) - 1:
                y = x + 1
                sorted = True

                while y < len(pages):
                    if pages[x] in rules:
                        # Found x|y, which is valid, increment y and continue
                        if pages[y] in rules[pages[x]]:
                            y += 1
                            continue

                    if pages[y] in rules:
                        # found y|x, which is invalid, swap them and restart the y loop from its beginning
                        if pages[x] in rules[pages[y]]:
                            # Swap them, restart the loop from x
                            temp = pages[x]
                            pages[x] = pages[y]
                            pages[y] = temp
                            sorted = False
                            swapped = True
                            break
                    
                    # Did not find x|y or y|x, just increment
                    y += 1

                if sorted:
                    # Got through the whole y loop without swapping anything, x is in order with everything in front of it, increment x
                    x += 1

            if swapped:
                # Only add the sum if we did any swap in the loop
                mid = int(pages[int(len(pages) / 2)])
                sum += mid
    print(sum)