import os
import sys

def read_file(file):
    return list(int(x) for x in open(os.path.join(sys.path[0],file)).read().split(","))


def part1(test = False):
    input = read_file("testinput.txt") if test else read_file("input.txt")

    for j in range(80):
        for i in range(len(input)): # refactor to map
            if input[i] == 0:
                input[i] = 6
                input.append(8)
            else:
                input[i] -= 1
        print(f"Day: {j}, Fishes: {len(input)}")
    return len(input)

print(f"Part 1: {part1(True)}")