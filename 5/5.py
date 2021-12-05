import os
import sys
import math
import sys

class Point:
    def __init__(self, x_init, y_init):
        self.X = int(x_init)
        self.Y = int(y_init)

    def __repr__(self):
        return "".join([str(self.X), ",", str(self.Y)])


lines = [list(x.replace(" -> ", "#").rstrip().split("#")) for x in open(os.path.join(sys.path[0],"input.txt")).readlines()]

newlines = []
for line in lines:
    # p1
    startX = line[0].split(",")[0]
    startY = line[0].split(",")[1]
    p1 = Point(startX, startY)

    # p2
    startX = line[1].split(",")[0]
    startY = line[1].split(",")[1]
    p2 = Point(startX, startY)
    newlines.append((p1, p2))

def distance(p1,p2):
    return math.sqrt((p1.X - p2.X)**2 + (p1.Y - p2.Y)**2)

# from, to , point to check
def is_between(a, b, c):
    crossproduct = (c.Y - a.Y) * (b.X - a.X) - (c.X - a.X) * (b.Y - a.Y)

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > sys.float_info.epsilon:
        return False

    dotproduct = (c.X - a.X) * (b.X - a.X) + (c.Y - a.Y)*(b.Y - a.Y)
    if dotproduct < 0:
        return False

    squaredlengthba = (b.X - a.X)*(b.X - a.X) + (b.Y - a.Y)*(b.Y - a.Y)
    if dotproduct > squaredlengthba:
        return False

    return True

# create matrix and set all to 0
matrix = [[0 for x in range(1000)] for y in range(1000)] 

def printmatrix(matrix):
    for x in matrix:
        print(x)

def countmatrix(matrix):
    # Count 2s in matrix
    return sum(x.count(2) for x in matrix)

for line in newlines:
    print(line)
    # print(x[0].Y)


    startX = line[0].X          # 0
    startY = line[0].Y          # 9
    #matrix[startX][startY] += 1

    endX = line[1].X            # 5
    endY = line[1].Y            # 9
    #matrix[endX][endY] += 1

    # loop Y
    if startX == endX:
        min_startY = min([startY, endY])
        max_endY = max([startY, endY])

        for i in range(min_startY, max_endY+1):
            #print(f"Append: {i},{startX}")
            if matrix[i][startX] == 0:
                matrix[i][startX] = 1
            elif matrix[i][startX] == 1:
                matrix[i][startX] = 2
            # matrix[i][startX] += 1

    # loop X
    if startY == endY:
        min_startX = min([startX, endX])
        max_endX = max([startX, endX])

        for i in range(min_startX, max_endX+1):
            #print(f"Append: {startY},{i}")
            if matrix[startY][i] == 0:
                matrix[startY][i] = 1
            elif matrix[startY][i] == 1:
                matrix[startY][i] = 2
            # matrix[startY][i] += 1


    

#printmatrix(matrix)
print(f"Part 1: {countmatrix(matrix)}")