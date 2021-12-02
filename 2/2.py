import os
import sys

lines = [x for x in open(os.path.join(sys.path[0],"input.txt")).readlines()]


# Part 1
x = 0
y = 0
for i in lines:
    direction = i.split(" ")[0]
    value = int(i.split(" ")[1])

    if direction == "forward":
        x += value
    if direction == "up":
        y -= value
    if direction == "down":
        y += value

print(f"Part 1: {x * y}")


# Part 2
x = 0
y = 0
aim = 0
for i in lines:
    direction = i.split(" ")[0]
    value = int(i.split(" ")[1])

    if direction == "forward":
        x += value
        y += aim * value
    if direction == "up":
        aim -= value
    if direction == "down":
        aim += value

print(f"Part 2: {x * y}")
