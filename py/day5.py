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