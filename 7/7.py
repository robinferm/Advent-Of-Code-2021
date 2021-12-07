import os
import sys

def read_file(file):
    return list(int(x) for x in open(os.path.join(sys.path[0],file)).read().split(","))

def calc_fuel(n):
    sum = 0
    for x in range(n+1):
        sum += x
    return sum

def part1(test=False):
    input = read_file("testinput.txt") if test else read_file("input.txt")

    dict = {str(x):0 for x in input}

    # Loop every possible destination
    for i in range(max(input)+1):
        totalfuel = 0
        
        # Loop all current positions
        for j in input:

            # part 1
            #totalfuel += abs(j-i)

            # Part 2
            test = calc_fuel(abs(i-j))

            totalfuel += test
            dict[str(i)] = totalfuel

    return min(dict.values())

print(part1())