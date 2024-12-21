import fileinput
import regex as re

def part1():

    sum = 0
    for line in fileinput.input(files="input/test_3.txt"):
        matches = re.findall('mul\\((\\d{1,3}),(\\d{1,3})\\)', line)
        for match in matches:
            product = int(match[0]) * int(match[1])
            sum += product
    print(sum)
            

def part2():

    sum = 0
    do = True
    for line in fileinput.input(files="input/test_3.txt"):
        # positive look behind for do()
        # '(?<=do\\(\\)).*?mul\\((\\d{1,3}),(\\d{1,3})\\)'
        # negative look behind for dont(), but eliminate all mul() after the 1st dont() appears
        # regex = '(?<!don\'t\\(\\).*?)mul\\((\\d{1,3}),(\\d{1,3})\\)'
        # positive lookbehind for do() that isn't interrupted (lookahead) by a dont() before the mul
        # regex2 = '(?<=do\\(\\).*? (?!don\'t\\(\\)))mul\\((\\d{1,3}),(\\d{1,3})\\)'
        regex = '(mul\\((\\d{1,3}),(\\d{1,3})\\))|(do\\(\\))|(don\'t\\(\\))'
        matches = re.findall(regex, line)
        for match in matches:
            match = [m for m in match if len(m) > 0]
            if (match[0] == 'do()'):
                do = True
            elif (match[0] == 'don\'t()'):
                do = False
            elif (match[0].startswith('mul')) and do:
                product = int(match[1]) * int(match[2])
                sum += product
        
    print(sum)