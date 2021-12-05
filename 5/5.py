import os
import sys
import sys
import numpy

class Point:
    def __init__(self, x_init, y_init):
        self.X = int(x_init)
        self.Y = int(y_init)

    def __repr__(self):
        return "".join([str(self.X), ",", str(self.Y)])

def read_file(file):
    return [list(x.replace(" -> ", "#").rstrip().split("#")) for x in open(os.path.join(sys.path[0],file)).readlines()]

def create_points(file):
    lines = read_file(file)
    points = []
    for line in lines:
        # p1
        startX = line[0].split(",")[0]
        startY = line[0].split(",")[1]
        p1 = Point(startX, startY)

        # p2
        startX = line[1].split(",")[0]
        startY = line[1].split(",")[1]
        p2 = Point(startX, startY)
        points.append((p1, p2))
    return points

def create_matrix(size):
    # create matrix and set all to 0
    matrix = [[0 for x in range(size)] for y in range(size)]
    return matrix

def print_matrix(matrix):
    for x in matrix:
        print(x)

def count_matrix(matrix):
    # Count greater than 1 in matrix
    arr = numpy.asarray(matrix)
    return (arr > 1).sum()







def part1(test = False):
    newlines = create_points("testinput.txt") if test else create_points("input.txt")
    matrix = create_matrix(10) if test else create_matrix(1000)
    for line in newlines:

        startX = line[0].X
        startY = line[0].Y
        endX = line[1].X
        endY = line[1].Y

        # loop Y
        if startX == endX:
            min_startY = min([startY, endY])
            max_endY = max([startY, endY])

            for i in range(min_startY, max_endY+1):
                matrix[i][startX] += 1

        # loop X
        if startY == endY:
            min_startX = min([startX, endX])
            max_endX = max([startX, endX])

            for i in range(min_startX, max_endX+1):
                matrix[startY][i] += 1

    return count_matrix(matrix)





def part2(test = False):
    newlines = create_points("testinput.txt") if test else create_points("input.txt")
    matrix = create_matrix(10) if test else create_matrix(1000)
    for line in newlines:

        startX = line[0].X
        startY = line[0].Y
        endX = line[1].X
        endY = line[1].Y

        # loop Y
        if startX == endX:
            min_startY = min([startY, endY])
            max_endY = max([startY, endY])

            for i in range(min_startY, max_endY+1):
                matrix[i][startX] += 1

        # loop X
        if startY == endY:
            min_startX = min([startX, endX])
            max_endX = max([startX, endX])

            for i in range(min_startX, max_endX+1):
                matrix[startY][i] += 1

        # Diagonal

        # \
        # Handle right to left
        if startX > endX and startY > endY:
            startX, endX = endX, startX
            startY, endY = endY, startY
        
        if startX < endX and startY < endY: # 0,0 -> 8,8 \ top -> bot
            sx = startX
            sy = startY
            while (sx != endX+1 and sy != endY+1):
                matrix[sy][sx] += 1
                sx += 1
                sy += 1
        # /
        # Handle right to left
        if startX > endX and startY < endY: # 
            startX, endX = endX, startX
            startY, endY = endY, startY

        if startX < endX and startY > endY: # 0,8 -> 8,0 / bot -> top
            sx = startX
            sy = startY
            while (sx != endX+1 and sy != endY-1):
                matrix[sy][sx] += 1
                sx += 1
                sy -= 1

    return count_matrix(matrix)

print(part1())
print(part2())