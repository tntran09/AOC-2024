import fileinput

def part1():
    lines = [line.strip() for line in fileinput.input(files="input/test_4.txt")]
    
    sum = 0
    # search rows for XMAS and SAMX
    for row in lines:
        forwards = '____'
        backwards = '____'

        for j in range(len(row)):
            forwards = forwards[1:] + row[j]
            backwards = row[j] + backwards[0:3]
            if (forwards == 'XMAS' or backwards == 'XMAS'):
                sum += 1
    # print(sum)

    for i in range(len(lines[0])):
        forwards = '____'
        backwards = '____'
        for j in range(len(lines)):
            forwards = forwards[1:] + lines[j][i]
            backwards = lines[j][i] + backwards[0:3]
            if (forwards == 'XMAS' or backwards == 'XMAS'):
                sum += 1
    # print(sum)

    # Down-right and up-left diagonals
    forwards = '____'
    backwards = '____'
    i = len(lines) - 4
    j = 0
    diagonal_length = 0
    while(True):
        forwards = forwards[1:] + lines[i][j]
        backwards = lines[i][j] + backwards[0:3]
        diagonal_length += 1
        if (forwards == 'XMAS' or backwards == 'XMAS'):
            sum += 1
        # Either increment down and right, reset to the next diagonal, or break
        if i < len(lines) - 1 and j < len(lines[i]) - 1:
            i += 1
            j += 1
        elif i == 3 and j == len(lines[i]) - 1:
            break
        else:
            forwards = '____'
            backwards = '____'
            i = i - diagonal_length + 1
            j = j - diagonal_length + 1
            if i > 0:
                i -= 1
            elif i == 0:
                j += 1
            diagonal_length = 0
    # print(sum)

    # Down-left and up-right diagonals
    forwards = '____'
    backwards = '____'
    i = 0
    j = 3
    diagonal_length = 0
    while(True):
        forwards = forwards[1:] + lines[i][j]
        backwards = lines[i][j] + backwards[0:3]
        diagonal_length += 1
        if (forwards == 'XMAS' or backwards == 'XMAS'):
            sum += 1
        # Either increment down and left, reset to the next diagonal, or break
        if i < len(lines) - 1 and j > 0:
            i += 1
            j -= 1
        elif i == len(lines) - 1 and j == len(lines[i]) - 4:
            break
        else:
            forwards = '____'
            backwards = '____'
            i = i - diagonal_length + 1
            j = j + diagonal_length - 1
            if j < len(lines[0]) - 1:
                j += 1
            elif j == len(lines[0]) - 1:
                i += 1
            diagonal_length = 0
    print(sum)

def part2():
    lines = [line.strip() for line in fileinput.input(files="input/test_4.txt")]
    sum = 0
    i = 1
    while i < len(lines) - 1:
        j = 0
        while j != -1:
            j = lines[i].find('A', j + 1)
            if j != -1 and j < len(lines[i]) - 1:
                corners = [lines[i - 1][j - 1], lines[i - 1][j + 1], lines[i + 1][j - 1], lines[i + 1][j + 1]]
                if corners == ['M','M','S','S'] or corners == ['M','S','M','S'] or corners == ['S','M','S','M'] or corners == ['S','S','M','M']:
                    sum += 1
        i += 1
    print(sum)