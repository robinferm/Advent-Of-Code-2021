import os
import sys

# with open("input.txt") as input:
#     lines = input.readlines()
    # lines = [line.rstrip() for line in lines]
lines = [int(x) for x in open("1/input.txt").readlines()]
lines = [int(x) for x in open(os.path.join(sys.path[0],"input.txt")).readlines()]


# Part 1 v1
total = 0
for x in range(1, len(lines)):
    if int(lines[x]) > int(lines[x-1]):
        total += 1
print(f"Part 1 v1: {total}")

# Part 1 v2
total = [x for x in range(1, len(lines)) if lines[x] > lines[x-1]]
print(f"Part 1 v2: {len(total)}")

# Part 1 v3
total = list(filter(lambda x: lines[x] > lines[x-1], range(len(lines))))
print(f"Part 1 v3: {len(total)}")





# Part 2
total = 0
for x in range(0, (len(lines)-1) - len(lines) % 3, 1):
    if sum(lines[x:x+3]) < sum(lines[x+1:x+4]):
        total += 1
print(f"Part 2: {total}")