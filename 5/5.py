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

def create_points():
    lines = read_file("input.txt")
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
    # Count 2s in matrix
    #return sum(x.count(2) for x in matrix)
    # Count greater than 1 in matrix
    arr = numpy.asarray(matrix)
    return (arr > 1).sum()







def part1():
    newlines = create_points()
    matrix = create_matrix(len(newlines)*2)
    for line in newlines:
        print(line)

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
                matrix[i][startX] += 1

        # loop X
        if startY == endY:
            min_startX = min([startX, endX])
            max_endX = max([startX, endX])

            for i in range(min_startX, max_endX+1):
                matrix[startY][i] += 1

    return count_matrix(matrix)




def part2():
    newlines = create_points()
    matrix = create_matrix(len(newlines)*2)
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


        # Diagonal
        # BÖrja alltid från vänster? 
        if startX < endX and startY < endY: # \ top > down
            print(f"Start: {startX} {startY}, end: {endX} {endY}")
            sx = startX
            sy = startY
            while (sx != endX and sy != endY):
                #matrix[sx][sy] = 5
                if matrix[sx][sy] == 0:
                    matrix[sx][sy] = 1
                elif matrix[sx][sy] == 1:
                    matrix[sx][sy] = 2
                # matrix[startY][i] += 1
                # x+1, y+1
                sx += 1
                sy += 1

        if startX > endX and startY < endY: # \ # bot > up
            print(f"Start: {startX} {startY}, end: {endX} {endY}")
            sx = startX
            sy = startY
            while (sx != endX and sy != endY):
                #matrix[sx][sy] = 5
                if matrix[sx][sy] == 0:
                    matrix[sx][sy] = 1
                elif matrix[sx][sy] == 1:
                    matrix[sx][sy] = 2
                #matrix[sx][sy] = 5
                # x+1, y-1
                sy += 1
                sx -= 1

        if startX < endX and startY > endY: # / # bot > up
            print(f"Start: {startX} {startY}, end: {endX} {endY}")
            sx = startX
            sy = startY
            while (sx != endX and sy != endY):
                #matrix[sx][sy] = 5
                if matrix[sx][sy] == 0:
                    matrix[sx][sy] = 1
                elif matrix[sx][sy] == 1:
                    matrix[sx][sy] = 2
                #matrix[sx][sy] = 5
                # x+1, y-1
                sy -= 1
                sx += 1

        if startX > endX and startY > endY: # / # bot > up
            print(f"Start: {startX} {startY}, end: {endX} {endY}")
            sx = startX
            sy = startY
            while (sx != endX and sy != endY):
                #matrix[sx][sy] = 5
                if matrix[sx][sy] == 0:
                    matrix[sx][sy] = 1
                elif matrix[sx][sy] == 1:
                    matrix[sx][sy] = 2
                #matrix[sx][sy] = 5
                # x+1, y-1
                sy -= 1
                sx -= 1

    print_matrix(matrix)
    return count_matrix(matrix)

print(part1())
#print(part2())        
        
        # x+1, y-1
    # if startY > endY: # / bot > up
    #     # y+1
    # if startY < endY: # \ top > down
    #     # y-1

    # min_startX = min([startX, endX])
    # max_endX = max([startX, endX])
    # for i in range(min_startX, max_endX+1):
        
    #     #print(f"Append: {startY},{i}")
    #     if matrix[startY][i] == 0:
    #         matrix[startY][i] = 1
    #     elif matrix[startY][i] == 1:
    #         matrix[startY][i] = 2
    #     # matrix[startY][i] += 1

    # min_startY = min([startY, endY])
    # max_endY = max([startY, endY])

    # for i in range(min_startY, max_endY+1):
    #     #print(f"Append: {i},{startX}")
    #     if matrix[i][startX] == 0:
    #         matrix[i][startX] = 1
    #     elif matrix[i][startX] == 1:
    #         matrix[i][startX] = 2
    #     # matrix[i][startX] += 1


# 00 01 02
# 10 11 12
# 20 21 22

# 00 11 22
# x+1
# y+1