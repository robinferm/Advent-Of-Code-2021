import os
import sys

def read_file(file):
    return list(int(x) for x in open(os.path.join(sys.path[0],file)).read().split(","))

def swap(dict, a, b):
    dict[str(a)], dict[str(b)] = dict[str(b)], dict[str(a)]

def part1_and_part2(test = False):
    input = read_file("testinput.txt") if test else read_file("input.txt")
    dict = {str(x): input.count(x) for x in range(9)}

    # Loop days
    for _ in range(256):

        temp = dict['0']
        dict['0'] = 0

        for i in range(len(dict.keys())-1):
            swap(dict, i, i+1)

        dict['8'] += temp
        dict['6'] += temp

    return sum(dict.values())

print(f"Part 1 and part 2: {part1_and_part2()}")