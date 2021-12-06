import os
import sys
import math

def read_file(file):
    return list(int(x) for x in open(os.path.join(sys.path[0],file)).read().split(","))

def part1_and_part2(test = False):
    input = read_file("testinput.txt") if test else read_file("input.txt")
    dict = {'0':input.count(0),
            '1':input.count(1),
            '2':input.count(2),
            '3':input.count(3),
            '4':input.count(4),
            '5':input.count(5),
            '6':input.count(6),
            '7':input.count(7),
            '8':input.count(8)}

    # Loop days
    for j in range(256):

        temp = dict['0']

        dict['0'] = 0

        dict['1'], dict['0'] = dict['0'], dict['1']
        dict['2'], dict['1'] = dict['1'], dict['2']
        dict['3'], dict['2'] = dict['2'], dict['3']
        dict['4'], dict['3'] = dict['3'], dict['4']
        dict['5'], dict['4'] = dict['4'], dict['5']
        dict['6'], dict['5'] = dict['5'], dict['6']
        dict['7'], dict['6'] = dict['6'], dict['7']
        dict['8'], dict['7'] = dict['7'], dict['8']

        dict['8'] += temp
        dict['6'] += temp

    return sum(dict.values())

print(f"Part 1 and part 2: {part1_and_part2()}")